#!/usr/bin/python
import os, TileStache

class Layers:
    def __init__(self, config, layers):
        self.config = config
        
        # each layer has a back-reference to config that we'll need to update.
        for name in layers:
            layers[name].config = config

        self._layers = layers

    def keys(self):
        return self._layers.keys()
    
    def items(self):
        return self._layers.items()
    
    def __contains__(self, name):
        return name in self._layers
    
    def __getitem__(self, name):
        """
        """
        if name not in self._layers and name == 'sample-choropleth':
            
            # Boilerplate needed to build up a layer in code:
            #   1. configuration object from self.config.
            #   2. projection object instantiated out of TileStache.Geography.
            #   3. a metatile, which is just 1x1 without any arguments.

            projection = TileStache.Geography.SphericalMercator()
            metatile = TileStache.Core.Metatile()
            layer = TileStache.Core.Layer(self.config, projection, metatile)

            # The provider needs a backreference to
            # the layer, so it's added after the fact.
            
            layer.provider = TileStache.Providers.Mapnik(layer, 'cities-choropleth.xml')
            self._layers[name] = layer

        return self._layers[name]

class WrapConfiguration:

    def __init__(self, config):
        self.cache = config.cache
        self.dirpath = config.dirpath
        self.layers = Layers(self, config.layers)

config = WrapConfiguration(TileStache.parseConfigfile('acetate.cfg'))

TileStache.cgiHandler(os.environ, config, debug=True)

