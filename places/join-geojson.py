""" Join multiple GeoJSON files into one on stdout.
"""
from sys import argv, stdout
from json import load, dump
from operator import add

if __name__ == '__main__':
    collections = [load(open(filename, 'r')) for filename in argv[1:]]
    features = reduce(add, [c['features'] for c in collections], [])
    dump({'type': 'FeatureCollection', 'features': features}, stdout)
