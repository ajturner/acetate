from os.path import exists
from csv import DictReader
from math import sin, cos, pi, hypot
from json import dump as dumpjson
from itertools import combinations
from optparse import OptionParser, OptParseError
from gzip import GzipFile
from copy import deepcopy
from random import choice, random

from PIL.Image import new as newimg
from PIL.ImageDraw import Draw as drawimg
from PIL.ImageFont import truetype

from anneal import Annealer

from ModestMaps import mapByCenterZoom
from ModestMaps.Geo import Location
from ModestMaps.OpenStreetMap import Provider
from ModestMaps.Core import Point, Coordinate

from shapely.geometry import Polygon

NE, ENE, ESE, SE, SSE, S, SW, WSW, WNW, NW, NNW, N, NNE = range(13)

# slide 13 of http://www.cs.uu.nl/docs/vakken/gd/steven2.pdf
placements = {NE: 0.000, ENE: 0.070, ESE: 0.100, SE: 0.175, SSE: 0.200,
              S: 0.900, SW: 0.600, WSW: 0.500, WNW: 0.470, NW: 0.400,
              NNW: 0.575, N: 0.800, NNE: 0.150}

optparser = OptionParser(usage="""%prog [options] <city input files>
""")

defaults = {
    'zoom': 5,
    'minutes': 1,
    'points': 'out-points.json',
    'labels': 'out-labels.json',
    'countries': 'Countries.csv',
    'countryfont': ('fonts/DejaVuSans.ttf', 12),
    'pop25mfont': ('fonts/DejaVuSans.ttf', 14),
    'pop250kfont': ('fonts/DejaVuSans.ttf', 12),
    'pop50kfont': ('fonts/DejaVuSans.ttf', 12),
    'popotherfont': ('fonts/DejaVuSans.ttf', 12)
    }

optparser.set_defaults(**defaults)

optparser.add_option('-c', '--countries', dest='countries',
                     type='string', help='Input filename for countries. Default value is "%(countries)s".' % defaults)

optparser.add_option('-p', '--points', dest='points',
                     type='string', help='Output filename for points. Default value is "%(points)s".' % defaults)

optparser.add_option('-l', '--labels', dest='labels',
                     type='string', help='Output filename for labels. Default value is "%(labels)s".' % defaults)

optparser.add_option('-m', '--minutes', dest='minutes',
                     type='float', help='Number of minutes to run annealer. Default value is %(minutes).1f.' % defaults)

optparser.add_option('-z', '--zoom', dest='zoom',
                     type='int', help='Map zoom level. Default value is %(zoom)d.' % defaults)

optparser.add_option('--country-font', dest='countryfont',
                     type='string', nargs=2, help='Font filename and point size for countries. Default value is "%s", %d.' % (defaults['popotherfont'][0], defaults['popotherfont'][1]))

optparser.add_option('--pop25m-font', dest='pop25mfont',
                     type='string', nargs=2, help='Font filename and point size for cities of population 2.5m+. Default value is "%s", %d.' % (defaults['pop25mfont'][0], defaults['pop25mfont'][1]))

optparser.add_option('--pop250k-font', dest='pop250kfont',
                     type='string', nargs=2, help='Font filename and point size for cities of population 250k+. Default value is "%s", %d.' % (defaults['pop250kfont'][0], defaults['pop250kfont'][1]))

optparser.add_option('--pop50k-font', dest='pop50kfont',
                     type='string', nargs=2, help='Font filename and point size for cities of population 50k+. Default value is "%s", %d.' % (defaults['pop50kfont'][0], defaults['pop50kfont'][1]))

optparser.add_option('--popother-font', dest='popotherfont',
                     type='string', nargs=2, help='Font filename and point size for smaller cities. Default value is "%s", %d.' % (defaults['popotherfont'][0], defaults['popotherfont'][1]))

def coin_flip():
    return choice((True, False))

def compare_places(this, that):
    this = -int(this.__class__ is Country), this.rank, -(this.population or 0)
    that = -int(that.__class__ is Country), that.rank, -(that.population or 0)
    
    return cmp(this, that)

class Country:

    def __init__(self, name, abbreviation, rank, zoom, land_area, population, location, position, font):
        self.name = name
        self.abbr = abbreviation
        self.rank = rank
        self.zoom = zoom
        self.area = land_area
        self.population = population
        self.location = location
        self.position = position
        
        self.buffer = 2
        self.use_abbr = False
        
        self._original = deepcopy(position)
        self._label_shape = None
        
        self._minwidth, self._minheight = font.getsize(self.abbr)
        self._maxwidth, self._maxheight = font.getsize(self.name)

        self._update_label_shape()

    def __repr__(self):
        return '<Country: %s>' % self.abbr
    
    def __hash__(self):
        return id(self)

    def __cmp__(self, other):
        return compare_places(self, other)

    def __unicode__(self):
        return unicode(self.use_abbr and self.abbr or self.name)
    
    def _update_label_shape(self):
        """
        """
        x, y = self.position.x, self.position.y
        
        if self.use_abbr:
            width, height = self._minwidth, self._minheight
        else:
            width, height = self._maxwidth, self._maxheight
        
        x1, y1 = x - width/2, y - height/2
        x2, y2 = x + width/2, y + height/2
        
        self._label_shape = Polygon(((x1, y1), (x1, y2), (x2, y2), (x2, y1), (x1, y1)))
    
    def label_bbox(self):
        return self._label_shape.envelope
    
    def mask_shape(self):
        return self._label_shape.buffer(self.buffer).envelope
    
    def move(self):
        self.use_abbr = coin_flip()
    
        width = self.use_abbr and self._minwidth or self._maxwidth
        height = self.use_abbr and self._minheight or self._maxheight
        
        x = (random() - .5) * width
        y = (random() - .5) * height
    
        self.position.x = self._original.x + x
        self.position.y = self._original.y + y
        
        self._update_label_shape()
    
    def placement_energy(self):
        width = self.use_abbr and self._minwidth or self._maxwidth
        
        x = 2 * (self.position.x - self._original.x) / width
        y = 2 * (self.position.y - self._original.y) / width
        
        return int(self.use_abbr) + hypot(x, y) ** 2
    
    def overlap_energy(self, other):
        if self.overlaps(other):
            return min(10.0 / self.rank, 10.0 / other.rank)

        return 0.0
    
    def overlaps(self, other, reflexive=True):
        overlaps = self.mask_shape().intersects(other.label_bbox())
        
        if reflexive:
            overlaps |= other.overlaps(self, False)

        return overlaps

    def in_range(self, other, reflexive=True):
        range = hypot(self._maxwidth + self.buffer*2, self._maxheight + self.buffer*2)
        distance = hypot(self.position.x - other.position.x, self.position.y - other.position.y)
        in_range = distance <= range
        
        if reflexive:
            in_range |= other.in_range(self, False)

        return in_range
    
class City:
    
    def __init__(self, name, rank, zoom, population, geonameid, location, position, font):
        self.name = name
        self.rank = rank
        self.zoom = zoom
        self.population = population
        self.geonameid = geonameid
        self.location = location
        self.position = position

        self.placement = NE
        self.radius = 4
        self.buffer = 2
        
        x1, y1 = position.x - self.radius, position.y - self.radius
        x2, y2 = position.x + self.radius, position.y + self.radius
        
        self._point_shape = Polygon(((x1, y1), (x1, y2), (x2, y2), (x2, y1), (x1, y1)))
        self._label_shape = None

        self._width, self._height = font.getsize(self.name)
        self._update_label_shape()

    def __repr__(self):
        return '<City: %s>' % self.name
    
    def __hash__(self):
        return id(self)

    def __cmp__(self, other):
        return compare_places(self, other)

    def __unicode__(self):
        return unicode(self.name)
    
    def _update_label_shape(self):
        """
        """
        x, y = self.position.x, self.position.y
        
        if self.placement in (NE, ENE, ESE, SE):
            x += self.radius + self._width/2
        
        if self.placement in (NW, WNW, WSW, SW):
            x -= self.radius + self._width/2

        if self.placement in (NW, NE):
            y -= self._height/2

        if self.placement in (SW, SE):
            y += self._height/2

        if self.placement in (ENE, WNW):
            y -= self._height/6

        if self.placement in (ESE, WSW):
            y += self._height/6
        
        if self.placement in (NNE, SSE, NNW):
            _x = self.radius * cos(pi/4) + self._width/2
            _y = self.radius * sin(pi/4) + self._height/2
            
            if self.placement in (NNE, SSE):
                x += _x
            else:
                x -= _x
            
            if self.placement in (SSE, ):
                y += _y
            else:
                y -= _y
        
        if self.placement == N:
            y -= self.radius + self._height / 2
        
        if self.placement == S:
            y += self.radius + self._height / 2
        
        x1, y1 = x - self._width/2, y - self._height/2
        x2, y2 = x + self._width/2, y + self._height/2
        
        self._label_shape = Polygon(((x1, y1), (x1, y2), (x2, y2), (x2, y1), (x1, y1)))
    
    def label_bbox(self):
        return self._label_shape.envelope
    
    def mask_shape(self):
        return self._label_shape.buffer(self.buffer).envelope.union(self._point_shape)
    
    def move(self):
        self.placement = choice(placements.keys())
        self._update_label_shape()
    
    def placement_energy(self):
        return placements[self.placement]
    
    def overlap_energy(self, other):
        if self.overlaps(other):
            return min(10.0 / self.rank, 10.0 / other.rank)

        return 0.0
    
    def overlaps(self, other, reflexive=True):
        overlaps = self.mask_shape().intersects(other.label_bbox())
        
        if reflexive:
            overlaps |= other.overlaps(self, False)

        return overlaps

    def in_range(self, other, reflexive=True):
        range = self.radius + hypot(self._width + self.buffer*2, self._height + self.buffer*2)
        distance = hypot(self.position.x - other.position.x, self.position.y - other.position.y)
        in_range = distance <= range
        
        if reflexive:
            in_range |= other.in_range(self, False)

        return in_range
    
class HighZoomCity(City):
    
    def __init__(self, name, rank, zoom, population, geonameid, location, position, font):
        self.name = name
        self.rank = rank
        self.zoom = zoom
        self.population = population
        self.geonameid = geonameid
        self.location = location
        self.position = position

        self.buffer = 2
        
        self._original = deepcopy(position)
        self._label_shape = None
        
        self._width, self._height = font.getsize(self.name)

        self._update_label_shape()

    def __repr__(self):
        return '<H.Z. City: %s>' % self.name
    
    def __hash__(self):
        return id(self)

    def _update_label_shape(self):
        """
        """
        x, y = self.position.x, self.position.y
        
        x1, y1 = x - self._width/2, y - self._height/2
        x2, y2 = x + self._width/2, y + self._height/2
        
        self._label_shape = Polygon(((x1, y1), (x1, y2), (x2, y2), (x2, y1), (x1, y1)))
    
    def mask_shape(self):
        return self._label_shape.buffer(self.buffer).envelope
    
    def move(self):
        x = (random() - .5) * self._width
        y = (random() - .5) * self._height
    
        self.position.x = self._original.x + x
        self.position.y = self._original.y + y
        
        self._update_label_shape()
    
    def placement_energy(self):
        x = 2 * (self.position.x - self._original.x) / self._width
        y = 2 * (self.position.y - self._original.y) / self._width
        
        return hypot(x, y) ** 2
    
    def overlap_energy(self, other):
        if self.overlaps(other):
            return min(10.0 / self.rank, 10.0 / other.rank)

        return 0.0
    
    def in_range(self, other, reflexive=True):
        range = hypot(self._width + self.buffer*2, self._height + self.buffer*2)
        distance = hypot(self.position.x - other.position.x, self.position.y - other.position.y)
        in_range = distance <= range
        
        if reflexive:
            in_range |= other.in_range(self, False)

        return in_range

class Places:

    def __init__(self):
        self._places = []
        self._energy = 0.0
        self._neighbors = {}
        self._moveable = []

    def __iter__(self):
        return iter(self._places)

    def add(self, place):
        self._neighbors[place] = set()
    
        for other in self._places:
            if not place.in_range(other):
                continue

            self._energy += place.overlap_energy(other)
            self._neighbors[place].add(other)
            self._neighbors[other].add(place)
    
        self._energy += place.placement_energy()
        self._places.append(place)
        
        if place.zoom <= 7:
            self._moveable.append(place)
        
        return self._neighbors[place]

    def energy(self):
        return self._energy
    
    def move(self):
        place = choice(self._moveable)
        
        for other in self._neighbors[place]:
            self._energy -= place.overlap_energy(other)

        self._energy -= place.placement_energy()

        place.move()
        
        for other in self._neighbors[place]:
            self._energy += place.overlap_energy(other)

        self._energy += place.placement_energy()

def postprocess_args(opts, args):
    """ Return inputfile, pointsfile, labelsfile, minutes, zoom, fonts after optparser.parse_args().
    """
    try:
        inputfiles = args[0:]
    except IndexError:
        raise OptParseError('Input filename is required.')
    
    for inputfile in inputfiles:
        if not exists(inputfile):
            raise OptParseError('Non-existent input filename: "%(inputfile)s".' % locals())

    minutes = opts.minutes

    if minutes <= 0:
        raise OptParseError('Minutes must be greater than 0: "%(minutes).1f".' % locals())
    
    fonts = {}
    
    fontfile, fontsize = opts.countryfont
    
    try:
        fontsize = int(fontsize)
    except ValueError:
        raise OptParseError('Bad font size for countries: "%(fontsize)s".' % locals())
    
    if not exists(fontfile):
        raise OptParseError('Non-existent font filename for counties: "%(fontfile)s".' % locals())
    
    fonts['country'] = truetype(fontfile, fontsize, encoding='unic')

    for opt in ('pop25mfont', 'pop250kfont', 'pop50kfont', 'popotherfont'):
        population = opt[3:-4]
        fontfile, fontsize = getattr(opts, opt)
        
        try:
            fontsize = int(fontsize)
        except ValueError:
            raise OptParseError('Bad font size for population %(population)s: "%(fontsize)s".' % locals())
        
        if not exists(fontfile):
            raise OptParseError('Non-existent font filename for population %(population)s: "%(fontfile)s".' % locals())
        
        fonts[population] = truetype(fontfile, fontsize, encoding='unic')
    
    zoom = opts.zoom
    countriesfile = opts.countries
    pointsfile = opts.points
    labelsfile = opts.labels
    
    return countriesfile, inputfiles, pointsfile, labelsfile, minutes, zoom, fonts

def location_point(lat, lon, zoom):
    """ Return a point that maps to pixels at the requested zoom level for 2^8 tile size.
    """
    try:
        osm = Provider()
    
        location = Location(float(lat), float(lon))
        coord = osm.locationCoordinate(location).zoomTo(zoom + 8)
        point = Point(coord.column, coord.row)
        
        return location, point
    except ValueError:
        raise Exception((lat, lon, zoom))

def load_places(countriesfile, inputfiles, fonts, zoom):
    """ Load a new Places instance from the named text files for a given zoom.
    """
    osm = Provider()
    places = Places()
    count = 0
    
    for row in DictReader(open(countriesfile, 'r'), dialect='excel'):
        if int(row['zoom']) > zoom:
            continue

        location, point = location_point(row['latitude'], row['longitude'], zoom)
        land_area = float(row['land area km'])
        population = int(row['population'])
        font = fonts['country']
        
        kwargs = {'name': row['name'].decode('utf-8'),
                  'abbreviation': row['abbreviation'].decode('utf-8'),
                  'land_area': land_area,
                  'population': population,
                  'font': font,
                  'zoom': int(row['zoom']),
                  
                  'location': location,
                  'position': point,
        
                  # subtract two because the biggest countries appear at z3
                  'rank': int(row['zoom']) - 2
                 }
        
        neighbors = places.add(Country(**kwargs))
        
        count += 1
        print '%5d)' % count, row['name'], location, point
        
        if neighbors:
            print '       is in range of', ', '.join([n.name for n in neighbors])
    
    for inputfile in inputfiles:
    
        input = inputfile.endswith('.gz') and GzipFile(inputfile, 'r') or open(inputfile, 'r')
    
        for row in DictReader(input, dialect='excel-tab'):
            if int(row['zoom']) > zoom:
                continue

            location, point = location_point(row['latitude'], row['longitude'], zoom)
            
            try:
                population = int(row['population'])
            except ValueError:
                population = None

            if population >= 2500000:
                font = fonts['25m']
            elif population >= 250000:
                font = fonts['250k']
            elif population >= 50000:
                font = fonts['50k']
            else:
                font = fonts['other']
            
            kwargs = {'name': row['name'].decode('utf-8'),
                      'population': population,
                      'font': font,
                      'zoom': int(row['zoom']),
                      
                      'geonameid': row['geonameid'],
                      'location': location,
                      'position': point,
            
                      # subtract three because the biggest cities appear at z4
                      'rank': int(row['zoom']) - 3
                     }
            
            if zoom >= 9:
                neighbors = places.add(HighZoomCity(**kwargs))
            else:
                neighbors = places.add(City(**kwargs))
            
            count += 1
            print '%5d)' % count, row['name'], location, point
            
            if neighbors:
                print '       is in range of', ', '.join([n.name for n in neighbors])
    
    return places

def bbox_polygon(bbox, provider, zoom):

    rectangle = bbox.envelope.exterior
    (x1, y1), (x2, y2) = rectangle.coords[0], rectangle.coords[2]

    coord1 = Coordinate(y1, x1, zoom + 8)
    coord2 = Coordinate(y2, x2, zoom + 8)

    location1 = provider.coordinateLocation(coord1)
    location2 = provider.coordinateLocation(coord2)
    
    lat1, lon1 = location1.lat, location1.lon
    lat2, lon2 = location2.lat, location2.lon
    
    return Polygon(((lon1, lat1), (lon1, lat2), (lon2, lat2), (lon2, lat1), (lon1, lat1)))

if __name__ == '__main__':
    
    opts, args = optparser.parse_args()
    countriesfile, inputfiles, pointsfile, labelsfile, minutes, zoom, fonts \
        = postprocess_args(opts, args)

    capitals = set( [geonameid.strip() for geonameid in open('Capitals.txt')] )
    places = load_places(countriesfile, inputfiles, fonts, zoom)

    print '-' * 80
    
    print len(places._moveable), 'moveable places vs.', len(places._places), 'others'

    print '-' * 80
    
    def state_energy(places):
        return places.energy()

    def state_move(places):
        places.move()
    
    places, e = Annealer(state_energy, state_move).auto(places, minutes, 50)

    print '-' * 80
    
    osm = Provider()
    point_features, label_features = [], []
    visible_places = []
    
    for place in sorted(places):
    
        is_visible = True
        
        for other in visible_places:
            if place.overlaps(other):
                print 'skip', place.name, 'because of', other.name
                is_visible = False
                break
        
        if not is_visible:
            continue
        
        visible_places.append(place)
        
        properties = {'name': unicode(place),
                      'rank': place.rank,
                      'population': place.population,
                      'geonameid': getattr(place, 'geonameid', None),
                      'capital': (getattr(place, 'geonameid', '') in capitals and 'yes' or 'no'),
                      'place': (place.__class__ is Country and 'country' or 'city')
                     }
    
        location = place.location
        point_geometry = {'type': 'Point', 'coordinates': (location.lon, location.lat)}
        
        point_features.append({'type': 'Feature',
                               'geometry': point_geometry,
                               'properties': properties
                              })
        
        label_geometry = bbox_polygon(place.label_bbox(), osm, zoom).__geo_interface__
        
        label_features.append({'type': 'Feature',
                               'geometry': label_geometry,
                               'properties': properties
                              })
    
    dumpjson({'type': 'FeatureCollection', 'features': point_features}, open(pointsfile, 'w'))
    dumpjson({'type': 'FeatureCollection', 'features': label_features}, open(labelsfile, 'w'))
    
    print 'Wrote %d points to %s and %s.' % (len(point_features), pointsfile, labelsfile)
    
    print '-' * 80
    
    map = mapByCenterZoom(osm, Location(0, 0), zoom, Point(2 ** (zoom + 8), 2 ** (zoom + 8)))
    
    if zoom > 5:
        map = mapByCenterZoom(osm, Location(40.078, -96.987), zoom, Point(1400, 800))
        map = mapByCenterZoom(osm, Location(38.889, -77.050), zoom, Point(1200, 900))
    
    img = map.draw(False) # newimg('RGB', (map.dimensions.x, map.dimensions.y), (0xFF, 0xFF, 0xFF))
    draw = drawimg(img)

    print '-' * 80
    
    sw = map.pointLocation(Point(-100, map.dimensions.y + 100))
    ne = map.pointLocation(Point(map.dimensions.x + 100, -100))
    
    previewed_places = [place for place in visible_places
                        if (sw.lat < place.location.lat and place.location.lat < ne.lat
                        and sw.lon < place.location.lon and place.location.lon < ne.lon)]
    
    for place in previewed_places:
        box = place.label_bbox().envelope.exterior
        coord1 = Coordinate(box.coords[0][1], box.coords[0][0], zoom + 8)
        coord2 = Coordinate(box.coords[2][1], box.coords[2][0], zoom + 8)
        
        loc1, loc2 = osm.coordinateLocation(coord1), osm.coordinateLocation(coord2)
        point1, point2 = map.locationPoint(loc1), map.locationPoint(loc2)
        
        draw.rectangle((point1.x, point1.y, point2.x, point2.y), fill=(0xEE, 0xEE, 0xEE))
    
    i = 1
    for (cityA, cityB) in combinations(previewed_places, 2):
        if cityA.overlaps(cityB):
            print '%03d:' % i, cityA.name, 'x', cityB.name
            i += 1

    for place in previewed_places:
        if place.__class__ is Country:
            continue
    
        location = place.location
        point = map.locationPoint(location)
        color = (place.__class__ is Country) and (0x66, 0x66, 0x66) or (0x00, 0x00, 0x99)
        
        draw.rectangle((point.x-1, point.y-1, point.x+1, point.y+1), fill=color)

    for place in previewed_places:
        box = place.label_bbox().exterior
        coords = [Coordinate(c[1], c[0], zoom + 8) for c in box.coords]
        locations = [osm.coordinateLocation(coord) for coord in coords]
        points = [map.locationPoint(location) for location in locations]
        
        x = min([point.x for point in points]) + place.buffer
        y = min([point.y for point in points]) + place.buffer

        if place.__class__ is Country:
            font = fonts['country']
        elif place.population >= 2500000:
            font = fonts['25m']
        elif place.population >= 250000:
            font = fonts['250k']
        elif place.population >= 50000:
            font = fonts['50k']
        else:
            font = fonts['other']
        
        draw.text((x, y), unicode(place), font=font, fill=(0x00, 0x00, 0x00))

    img.save('out.png')
    
    print 'Saved preview map to out.png.'
