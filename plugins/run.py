import sys
import serial

#for line in sys.stdin:
#	print(line);

ser = serial.Serial('COM3', 9600)

data = ser.readline()
if data:
    print(data)