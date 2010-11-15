#!/usr/bin/python
import os, TileStache
TileStache.cgiHandler(os.environ, 'acetate.cfg', debug=True)

