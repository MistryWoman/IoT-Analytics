import os
import serial
import time
from time import sleep
from datetime import datetime
ser=serial.Serial("/dev/ttyACM0",baudrate=9600,timeout=1)
while 1:
		stra=ser.readline()
		#print(len(stra)) checkpoint for debugging
		
		if(len(stra)>0):
			now=datetime.now()
			nowstr=str(now)
			a=len(stra)
			b=len(nowstr)
			str1=stra+"    "+nowstr
			f=open("data.txt","a+")
			f.write("%s \n" % (str1))
			print(str1)
			
			
			
