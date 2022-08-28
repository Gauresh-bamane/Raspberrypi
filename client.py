import serial
import time
import paho.mqtt.client as mqtt
import string


ser = serial.Serial("/dev/rfcomm0", 9600)
ser.write(str.encode('Start\r\n'))

def on_connect(client, userdata, flags, rc): # func for making connection
	print("Connected to MQTT")
	print("Connection returned result: " + str(rc) )
	
	client.subscribe("ifn649")
def on_message(client, userdata, msg): # Func for Sending msg
	s="".join(map(chr,msg.payload))
	m= float(s)
	switch(m, s)
	
def switch(m,s):
    if m < 60:
        print("Led status: ON"+"|"+"Humidity is : "+ s +"C")
        ser.write(str.encode('LLED_ON'))
    else:
        print("Led status: OFF"+ "|" + "Humidity is :" + s + "C")
        ser.write(str.encode('LLED_OFF'))
        
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("13.54.211.159", 1883, 60)

client.loop_forever()

