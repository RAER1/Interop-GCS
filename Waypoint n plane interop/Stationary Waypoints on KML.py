'''Generate a KML string that matches the altitudemode example.

References:
http://code.google.com/apis/kml/documentation/kmlreference.html#gxaltitudemode
http://code.google.com/apis/kml/documentation/kmlfiles/altitudemode_reference.kml
'''

from pykml.factory import KML_ElementMaker as KML
name_object = KML.name("MPline2")
from pykml.factory import ATOM_ElementMaker as ATOM
from pykml.factory import GX_ElementMaker as GX
from pykml.factory import write_python_script_for_kml_document
from lxml import etree
import time

url = 'http://code.google.com/apis/kml/documentation/kmlfiles/altitudemode_reference.kml'
from pykml import parser
import urllib2

#lat = 29;
#lon = -81;
#alt = 0;

def waypoint(lat,lon,alt):
    wp = KML.Placemark(
        KML.Style(id='default'),
        KML.Point(
            KML.coordinates(str(lon) + "," + str(lat) + "," + str(alt))
        )
    )
    return wp

#while True:
    #lat = lat + .1
    #lon = lon + .1
with open("takeoff search land.txt", 'r') as waypointFile:
    filedata = waypointFile.read()

lines = filedata.split('\n')
del(lines [0])
del(lines [1])
wps = ()
strCoords = ''
for line in lines:
    try:
        cells = line.split('\t')
        lat = cells[8]
        lon = cells[9]
        alt = cells[10]
        wps = wps + (waypoint(lat,lon,alt),)
        strCoords = strCoords + '\n' + str(lon) + "," + str(lat) + "," + str(alt)
    except:
        pass
    print(cells)

wpLines = KML.Placemark(
    KML.Style(id='default'),
        KML.LineString(
            KML.coordinates(strCoords)
        )
)
    #tmp = {"x":str(wp.x),"y":str(wp.y),"z":str(wp.z)}

# fileobject = urllib2.urlopen(url)
# doc = parser.parse(fileobject).getroot()
# script = write_python_script_for_kml_document(doc)
# print script
print(wps)
root = KML.kml(KML.Folder(*(wps + (wpLines,))))
docString = etree.tostring(root, pretty_print=True, encoding='UTF-8')
f = open("waypoint.kml",'w')
f.write(docString)
f.close()
