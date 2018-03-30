import sys
import serial

#for line in sys.stdin:
#	print(line);

import subprocess
import json

input = sys.stdin.readline()
data = json.loads(input)

subprocess.call("meter.bash")

ser = serial.Serial('/dev/' + data["port"], 9600)

data = ser.readline()
while data:
	print(data)
	data = ser.readline()
