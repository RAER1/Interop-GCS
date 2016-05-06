# obsStationary = [{'latitude': 10, 'longitude': 5,  'cylinder_radius': 10, 'cylinder_height': 20}]
# obsMoving = [{'latitude': 0, 'longitude': 0, 'altitude_msl': 0, 'sphere_radius': 0}]


import clr
#import time
#include "mavlink/v1.0/ardupilotmega/mavlink.h"
from time import sleep
#import C\:\Program Files (x86)\Mission Planner
clr.AddReference("MissionPlanner.Utilities")
import MissionPlanner
import sys
sys.path.append(r"c:\Python27\Lib")
sys.path.append(r"c:\Python27\Lib\site-packages")
sys.path.append(r"C:\Program Files (x86)\Mission Planner")
#import serial, os, threading
import socket
import json
clr.AddReference("MAVLink")
#import MAVLink
UDP_IP = "127.0.0.1"
UDP_PORT = 54345
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Created Socket")
print("Bound Socket")

#Test out math!
yay = 10*13
print yay

#Script.ChangeMode('Auto')
#print("Set mode to Auto")

#print cs.alt
#print cs.wpno
#send_mavlink(MAV_CMD_NAV_LOITER_UNLIM)
#Script.ChangeMode("LOITER_UNLIM")
#print 'Returning to Launch'
#send_mavlink(MAV_CMD_NAV_TAKEOFF)
#print 'RTL'
sock.bind((UDP_IP, 54346))

#MAV.doCommand(MAVLink.VEHICLE_CMD_NAV_WAYPOINT, 0, 0, 10, 0, 0, 0, 0);
while 1 == 1:
	#print("Mode: ", str(cs.mode), "   WP Number: ", str(cs.wpno), "   Armed: ", str(cs.armed))
	#if cs.mode == "Auto" and cs.wpno == 1 and cs.armed == True:
		#print("launching")
		#ser = serial.Serial("com20",57600)
		#ser.write(bytes(0x0A))
		#sleep(0.1)
		#ser.close()
    #if cs.mode == "Auto" and cs.armed == True:


#	WPs = {"x":[], "y":[], "z":[]}
	WPs = []
	for wp in MissionPlanner.MainV2.comPort.MAV.wps.Values:
#		WPs["x"] = WPs["x"] + [str(wp.x)]
#		WPs["y"] = WPs["y"] + [str(wp.y)]
#		WPs["z"] = WPs["z"] + [str(wp.z)]
		tmp = {"x":str(wp.y),"y":str(wp.x)}
#		print(tmp)
		WPs = WPs + [tmp]
	#print("Sending.....")
	acInfo = {"Altitude":str(cs.alt),"Heading":str(cs.yaw)}
	aircraft = [{"x":str(cs.lng), "y":str(cs.lat)}]
	data = {"Waypoints":WPs, "Aircraft":aircraft,"Info":acInfo}

	tmp = json.dumps(data)
	#print(tmp)
	sock.sendto(tmp,(UDP_IP, UDP_PORT))
	#print("Sent JSON Data over UDP")
	sleep(.05)
sock.close()
#sock.bind((UDP_IP, UDP_PORT))
#sock.recv(bytes)