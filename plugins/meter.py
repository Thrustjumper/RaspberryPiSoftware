import sys
import serial
import os
import json

input = sys.stdin.readline()
data = json.loads(input)

os.system("sudo bash meter.bash")

ser = serial.Serial('/dev/' + data["port"], baudrate=300, bytesize=7, parity=1,stopbits=1)

data = ser.readline()
while data:
	print(data)
	data = ser.readline()
