from pykml.factory import KML_ElementMaker as KML
from lxml import etree

f = open("testingspherey.kml",'w')
sphere = KML.Placemark(
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
    )

print(etree.tostring(poly1, pretty_print=True))
fld = KML.kml(poly1)
polystr = etree.tostring(fld, pretty_print=True)
f.write(polystr)
f.close()