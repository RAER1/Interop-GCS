import math
from pykml.factory import KML_ElementMaker as KML
from lxml import etree

def cylinder(lat, lon, alt, rad, res):
	rlat = math.radians(lat)
	#lat per meter
	mPLat = 111132.92 - 559.82 * math.cos(2* rlat) + 1.175*math.cos(4*rlat);
	latPm = 1/mPLat
	#lon per meter
	mPLon = 111412.84 * math.cos(rlat) - 93.5 * math.cos(3*rlat);
	lonPm = 1/mPLon
	points = []
	for theta in range(0,res):
		x = rad*math.cos(math.radians(360*theta/res))
		y = rad*math.sin(math.radians(360*theta/res))
		latitude = lat + latPm*y
		longitude = lon + lonPm*x
		point = {'lon': longitude, 'lat': latitude, 'alt':alt}
		points = points + [point]
	points += [points[0]]
	pointStrs = ""
	for point in points:
		pointStrs += str(point['lon']) + "," + str(point['lat']) + "," + str(point['alt']) + " "
	style1 = KML.Style(
		KML.PolyStyle(
		KML.color("aaff00"),
		),
	)
	cylinder_obj = KML.Placemark(
			KML.Style(
				KML.PolyStyle(
					KML.color("8f0000ff"),
				),
				KML.LineStyle(
					KML.color("000000ff"),
				),
			),
			KML.Polygon(
            KML.extrude('1'),
			KML.tessellate('1'),
            KML.altitudeMode('relativeToGround'),
            KML.outerBoundaryIs(
              KML.LinearRing(
                KML.coordinates(pointStrs),
              ),
            ),
          ))
	return cylinder_obj

