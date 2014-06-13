#!/usr/bin/env python
from __future__ import print_function
import sys
import math

# import library
from geographiclib.geodesic import Geodesic

ourlat = # Your latitude (+: North, -: South)
ourlon = # Your longitude (+: East, -: West)
nmtometers = 1852 # 1 nautical mile = 1852 meters
latlonlimit = 3 # in degrees
nmlimit = 45 # in nautical miles

for line in sys.stdin:
    words = line.split()
    try: 
        dlat = float(words[2])
    except ValueError:
        continue
    try: 
        dlon = float(words[3])
    except ValueError:
        continue
    if (abs(dlat - ourlat) >= latlonlimit) or (abs(dlon - ourlon) >= latlonlimit):
        # out of bound
        continue
    calc = Geodesic.WGS84.Inverse(ourlat, ourlon, dlat, dlon)
    if calc['azi1'] < 0:
        azi = calc['azi1'] + 360
    else:
        azi = calc['azi1']
    nmdist = calc['s12'] / nmtometers
    dx = nmdist * math.sin(azi * math.pi / 180)
    dy = nmdist * math.cos(azi * math.pi / 180)
    # limit the nautical mile values
    if (abs(dx) <= nmlimit) and (abs(dy) <= nmlimit):
        print(nmdist, azi)
