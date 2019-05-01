# Test program is a slightly modified version of Odunlade Emmanuel's program
# of CircuitDigest where you can find a guide to implementing GPS on the Pi
import time
import serial
import pynmea2
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

port = "/dev/ttyAMA0"
ser = serial.Serial(port, baudrate = 9600, timeout = 0.5)

try:
	
	while 1:
		try:
			data = ser.readline()
		except:
			print("Loading...")
			
			
		if data[0:6] == "$GPGGA":
			msg = pynmea2.parse(data)
			latval = msg.lat
			concatlat = "Lat: " + str(latval)

                        lonval = msg.lon
                        concatlon = "Lon: " + str(lonval)

			print(concatlat)
                        print(concatlon)

			time.sleep(2)
			
except:
	time.sleep(2)
