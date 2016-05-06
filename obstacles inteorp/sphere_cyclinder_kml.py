import math
from pykml.factory import KML_ElementMaker as KML
from lxml import etree

def circle(lat, lon, alt, rad, res):
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
	print(points[0])
	return points
	
if __name__ == "__main__":
	lat = 29
	lon = -82
	rad = 40
	res = 10
	alt = 10
	points = circle(lat,lon,alt,rad,res)
	#print(points)
	name_object = KML.name("Hello World!")
	f = open("testingCircle.kml",'w')
	pointStrs = ""
	for point in points:
		pointStrs += str(point['lon']) + "," + str(point['lat']) + "," + str(point['alt']) + " "
	style1 = KML.Style(
		KML.PolyStyle(
		KML.color("aaff00"),
		),
	)
	poly = KML.Placemark(
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
          ),

    poly1 = KML.Placemark(
    	KML.name('Spherey'),
        KML.Style(id='default'),
	    KML.Model(
                KML.altitudeMode('relativeToGround'),
                KML.Location(
                    KML.longitude('-105'),
                    KML.latitude('40'),
                    KML.altitude('600'),
                ),
                KML.Orientation(
                    KML.heading('-0'),
                    KML.tilt('0'),
                    KML.roll('0'),
                ),
                KML.Scale(
                    KML.x('1'),
                    KML.y('1'),
                    KML.z('1'),
                ),
                KML.Link(
                    KML.href('sphere1.dae'),
                ),
                KML.ResourceMap(
                    KML.Alias(
                        KML.targetHref('texture.jpg'),
                        KML.sourceHref('untitled/texture.jpg'),
                    ),
                ),
            ),
        ),

    fld = KML.Folder(poly),
    fld1 = KML.Folder(poly1),
    polystr = etree.tostring(fld, pretty_print=True)
    polystr1  = etree.tostring(fld1,pretty_print=True)
    f.write(polystr)
    f.close()