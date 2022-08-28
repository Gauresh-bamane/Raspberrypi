
import serial
import time
import paho.mqtt.client as mqtt
import string

def on_connect(client, userdata, flags, rc): # func for making connection
	print("Connected to MQTT")
	print("Connection returned result: " + str(rc) )
	
	client.subscribe("ifn649")
def on_message(client, userdata, msg): # Func for Sending msg
	s=''.join(map(chr,msg.payload))
	m= float(s)
	if m >= 30:
		print("LED STATUS: ON"+"|"+"TEMPRATURE is : "+ s +"C")
		ser.write(str.encode('LLED_ON'))
	else:
		print("LED STATUS: OFF"+ "|" + "TEMPRATURE is :" + s + "C")
		ser.write(str.encode('LLED_OFF'))
	

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("13.54.211.159", 1883, 60)

client.loop_forever()
