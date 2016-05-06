__author__ = 'Robotics'
from pykml.factory import KML_ElementMaker as KML
def sphere (lat, lon, alt, rad):
    sphere_obj = KML.Placemark(
	    KML.name('Spherey'),
        KML.Style(id='default'),
	    KML.Model(
              KML.altitudeMode('relativeToGround'),
              KML.Location(
                  KML.longitude(str(lon)),
                  KML.latitude(str(lat)),
                  KML.altitude(str(alt)),
              ),
              KML.Orientation(
                  KML.heading('-0'),
                  KML.tilt('0'),
                  KML.roll('0'),
                ),
                KML.Scale(
                    KML.x(str(rad/25)),
                    KML.y(str(rad/25)),
                    KML.z(str(rad/25)),
                ),
                KML.Link(
                    KML.href("C:\Users/robot\Google Drive\SUAS\SUAS 2016\GCS Interop\obstacles inteorp\cgi-bin\sphere1.dae"),
                ),
                KML.ResourceMap(
                    KML.Alias(
                        KML.targetHref('texture.jpg'),
                        KML.sourceHref('untitled/texture.jpg'),
                    ),
                ),
            ),
        )
    return sphere_obj
