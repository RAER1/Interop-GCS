__author__ = 'RAER'
#!/usr/bin/env python
'''Generate a KML string that matches the altitudemode example.

References:
http://code.google.com/apis/kml/documentation/kmlreference.html#gxaltitudemode
http://code.google.com/apis/kml/documentation/kmlfiles/altitudemode_reference.kml
'''

from lxml import etree
from pykml.parser import Schema
from pykml.factory import KML_ElementMaker as KML
from pykml.factory import GX_ElementMaker as GX
from get_sphere import sphere
import socket
import json
import urllib2

UDP_IP = "127.0.0.1"
UDP_PORT = 54345

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(2000) # buffer size is 1024 bytes
    #print "received message:", data
    data2 = json.loads(data)
    #print data2['Info']
    #print data2['Waypoints']


    #To put into GE
    name_object = KML.name("MPline2")
    f = open("..\\Fluffy.kml",'w')

    #url = 'http://code.google.com/apis/kml/documentation/kmlfiles/altitudemode_reference.kml'
    f.write ('<?xml version="1.0" encoding="UTF-8"?>\n<kml xmlns="http://www.opengis.net/kml/2.2">\n')




    #fileobject = urllib2.urlopen(url)
    #doc = parser.parse(fileobject).getroot()
    #script = write_python_script_for_kml_document(doc)
    #print script

    assert isinstance(KML, object)
    doc = KML.kml(
        KML.Placemark(
            KML.name("gx:altitudeMode Example"),
            KML.LookAt(
                KML.longitude(data2['Waypoints']),                             #-79.806),
                KML.latitude(data2['Waypoints']),                                     #-12.219),
                KML.heading(data2['Info']),
                KML.tilt(70),
                KML.altitude(data2['Info']),
                GX.altitudeMode("relativeToGround"),
            ),
            KML.LineString(
                KML.extrude(1),
                GX.altitudeMode("relativeToGround"),
                KML.coordinates(
                "data2['Waypoints']['Altitude']"                                #"-79.825,-12.233,400 "
                "data2['Waypoints']['Altitude']"                              #"-79.820,-12.222,400 "
                "data2['Waypoints']['Altitude']"                                #"-79.812,-12.212,400 "
                "data2['Waypoints']['Altitude']"                                #"-79.796,-12.209,400 "
                "data2['Waypoints']['Altitude']"                                #"-79.788,-12.205,400"
                ),
            ),
        ),
    )

polys = ()
for Obstacle in StationaryObstacles:
    polys = polys + (cylinder(Obstacle['lat'],Obstacle['lng'],Obstacle['alt'],Obstacle['rad'],Obstacle['res']),)

foo = etree.tostring(KML.Folder(*doc), pretty_print=True, encoding='UTF-8')
f.write(foo)
f.write( '</kml>')
f.close()
f = open("..\\Fluffy.kml",'r')
print(f.read())
f.close()

print etree.tostring(doc, pretty_print=True)

#output a KML file (named based on the Python script)
outfile = file(__file__.rstrip('.py')+'.kml','w')
outfile.write(etree.tostring(doc, pretty_print=True))

assert Schema('kml22gx.xsd').validate(doc)

# This validates:
# xmllint --noout --schema ../../pykml/schemas/kml22gx.xsd altitudemode_reference.kml


