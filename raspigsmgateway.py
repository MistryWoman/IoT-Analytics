import serial
import time
import os

ser=serial.Serial("/dev/ttyAMA0",9600,timeout=0)
while(1):
 ser.flush()
 time.sleep(1)
 ser.write('AT+CMGL="ALL"\r')
 time.sleep(1)
 r=ser.read(1000) #read 1000 bytes of data from incoming message
 print(r)
 
  if 'Parking spot is occupied' in r:
   print('Parking spot is occupied')
   time.sleep(2)
   t=ser.read(1000) #read 1000 bytes of data from the serial port reading sms
   print(t)
   time.sleep(3)
  else:
   print('No activity')
   time.sleep(2)
   t=ser.read(1000) 
   print(t)
  
ser.close()  