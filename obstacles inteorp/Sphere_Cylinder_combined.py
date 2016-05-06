import math
from pykml.factory import KML_ElementMaker as KML
from lxml import etree
from get_cylinder import cylinder
from get_sphere import sphere

StationaryObstacles = [{'lat': 29.01499, 'lng': -81.099, 'alt': 300, 'rad': 25, 'res': 40}, {'lat': 29.014, 'lng': -81.099, 'alt': 300, 'rad': 25, 'res': 40}]
MovingObstacles = [{'lat': 29.011657, 'lng': -81.097302, 'alt': 300, 'rad': 25}, {'lat': 29.016, 'lng': -81.098, 'alt': 300, 'rad': 25}]
polys = ()
for Obstacle in StationaryObstacles:
	polys = polys + (cylinder(Obstacle['lat'],Obstacle['lng'],Obstacle['alt'],Obstacle['rad'],Obstacle['res']),)
for Obstacle in MovingObstacles:
	polys = polys + (sphere(Obstacle['lat'], Obstacle['lng'],Obstacle['alt'], Obstacle['rad']),)


kml = KML.kml(KML.Folder(*polys))

kmlStr = etree.tostring(kml, pretty_print=True)
f = open('obstacles.kml','w')
f.write(kmlStr)
f.close()