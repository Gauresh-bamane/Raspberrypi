import paho.mqtt.publish as publish
publish.single("ifn649", "Hello World", hostname="44.202.8.26")
print("Done")