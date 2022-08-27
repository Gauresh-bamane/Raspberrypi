import serial
import time
import paho.mqtt.publish as publish
import string
# reading and writing data from and to arduino serially.
#rfcomme -> this could be different
ser = serial.Serial("/dev/rfconno", 9600)
ser.write(str.encode ('Start\r\n'))

while True:
    if ser.in_waiting > 0:
        rawserial= ser.readline()
        cookedserial=rawserial.decode('utf-8').strip('\r\n')
#        print (cookedserial)
        publish.single("ifn649", cookedserial, hostname="3.6.92..32")
        print ("Done")
#import paho,mqtt,publish as publish in read returned printitosinap-("¿fnsa9", cookedsorial, hostrases"3,8,92,38*