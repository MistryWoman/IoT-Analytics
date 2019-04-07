import os
import serial
import time
import sys
import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime
try:
	import urllib.request as urllib2
except ImportError:
		import urllib2
		
		
ser=serial.Serial("/dev/ttyACM0",baudrate=9600,timeout=1)
count=0
DEBUG=1
RCpin=24
myAPI="QP5I9LCKYDNUV7CH"
myDELAY= 15

def getSensordata():

	while 1:
		stra=ser.readline()
		
		if(len(stra)>0):
			
			now=datetime.now()
			nowstr=str(now)
			str1=stra+" : "+nowstr
			
			f=open("parkingdata.txt","a+")
			f.write("%s\n" %(str1))
			print(str1)
			f.close()
			
def main():
print('starting....')
baseURL='https://api.thingsspeak.com/update?api_key=QP5I9LCKYDNUV7CH&field1=0'
print(baseURL)
while True:
 try: 
		mag=getSensordata()
		f= urllib2.urlopen(baseURL + "&field1=%s" % (mag))
		if(i<10):
		
			print(f.read())
			print(status)
			i=i+1
			
		f.close()
		sleep(int(myDELAY))
		
 except:
		print('exiting')
		#break
main()		