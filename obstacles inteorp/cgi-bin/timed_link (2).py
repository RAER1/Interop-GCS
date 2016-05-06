#!/usr/bin/python
print "Content-Type: text"     # HTML is following
print                               # blank line, end of headers

import random
import time
import math
from pykml.factory import KML_ElementMaker as KML
from lxml import etree
from get_cylinder import cylinder
from get_sphere import sphere
import json
import sys

f = open("..\\Linked.kml",'w')
lat = random.random() * 0.001 + 29.
lon = random.random() * 0.001 - 81.

now = time.time()
future = time.gmtime(now + 0.3)
y = future[0]
mo = future[1]
d = future[2]
h = future[3]
mi = future[4]
s = future[5]
iso8601 = '%04d-%02d-%02dT%02d:%02d:%02dZ' % (y,mo,d,h,mi,s)

StationaryObstacles = [{u'lat': 29.014993532, u'lng': -81.099345554, u'alt': 300, u'rad': 25, u'res': 40}, {u'lat': 29.014, u'lng': -81.099, u'alt': 300, u'rad': 25, u'res': 40}]
MovingObstacles = [{u'lat': 29.01165723255, u'lng': -81.097302345553, u'alt': 300, u'rad': 25}, {u'lat': 29.016, u'lng': -81.098, u'alt': 300, u'rad': 25}]
# print(StationaryObstacles)
# print(MovingObstacles)


#	f.write ('Content-type: application/vnd.google-earth.kml+xml')
f.write ('<?xml version="1.0" encoding="UTF-8"?>\n<kml xmlns="http://www.opengis.net/kml/2.2">\n')

h = open('C:/Users/robot/Google Drive/SUAS/SUAS 2016/GCS Interop/obstacles inteorp/cgi-bin/obs.txt','r')
try:
	s = h.read()
	data = json.loads(s,encoding='utf-8')
except:
	#print 'loading data error'
	pass
h.close()
StationaryObstacles = data[0]
MovingObstacles = data[1]
polys = ()
for Obstacle in StationaryObstacles:
	polys = polys + (cylinder(Obstacle['lat'],Obstacle['lng'],Obstacle['alt'],Obstacle['rad'],Obstacle['res']),)
for Obstacle in MovingObstacles:
	polys = polys + (sphere(Obstacle['lat'], Obstacle['lng'],Obstacle['alt'], Obstacle['rad']),)

# must be child of <kml>
NLinkStr =	'<NetworkLinkControl>\n' + '<expires>%s</expires>' % iso8601 + '\n</NetworkLinkControl>\n'
f.write(NLinkStr)

foo = etree.tostring(KML.Folder(*polys), pretty_print=True, encoding='UTF-8')
f.write(foo)
f.write( '</kml>')
f.close()
f = open("..\Linked.kml",'r')
print(f.read())
f.close()
