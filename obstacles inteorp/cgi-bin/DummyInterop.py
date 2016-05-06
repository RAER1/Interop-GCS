__author__ = 'Robotics'

import sys
import json
from time import sleep
import random

lat = 29
lon = 81
alt = 150

while True:
    lat = lat + 0.000001
    lon = lon + 0.000001

    StationaryObstacles = ({'lat': random.random() * 0.0001 + lat,
                        'lng': random.random() * 0.00001 - lon,
                        'alt': random.random( )+ alt,
                        'rad': 25,
                        'res': 40},
                       {'lat': random.random() * 0.0001 + lat,
                        'lng': random.random() * 0.00001 - lon,
                        'alt': random.random( )+ alt,
                        'rad': 25,
                        'res': 40});
    MovingObstacles = ({'lat': random.random() * 0.0001 + lat,
                    'lng': random.random() * 0.00001 - lon,
                    'alt': random.random( )+ alt,
                    'rad': 25},
                   {'lat': random.random() * 0.0001 + lat,
                    'lng': random.random() * 0.00001 - lon,
                    'alt': random.random( )+ alt,
                    'rad': 25});
    f = open('obs.txt','w')
    json.dump([StationaryObstacles, MovingObstacles],f,encoding='utf-8')
    f.close()
    sleep(0.02)