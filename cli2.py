import paho.mqtt.client as mqtt
import time
import thread
import random

def on_connect(client, userdata, rc):
	print("Connected with result code" + str(rc))
	#client.subscribe("/data/from/tesensor1")
	
	
def on_message(client, userdata, msg):
	print(msg.topic + " " + str(msg.payload))
	
client = mqtt.Client("Sensor1")
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

client.loop_start()

client1 = mqtt.Client("Sensor2")
client1.on_connect = on_connect
client1.on_message = on_message

client1.connect("localhost", 1883, 60)

client1.loop_start()

client2 = mqtt.Client("Sensor3")
client2.on_connect = on_connect
client2.on_message = on_message

client2.connect("localhost", 1883, 60)

client2.loop_start()

client3 = mqtt.Client("Sensor4")
client3.on_connect = on_connect
client3.on_message = on_message

client3.connect("localhost", 1883, 60)

client3.loop_start()

client4 = mqtt.Client("Sensor5")
client4.on_connect = on_connect
client4.on_message = on_message

client4.connect("localhost", 1883, 60)

client4.loop_start()


#i = 0;
#while i < 10:
	#time.sleep(5)
	#client.publish("/data/from/tesensor1", "value=45")
	#time.sleep(5)
	#client1.publish("/data/from/tesensor2", "value=30")
	#i = i + 1
	
#client.loop_stop()
#client1.loop_stop()

#client.disconnect()
#client1.disconnect()	
def publishTemp(clientt, topic, delay_time, count):
	while count > 0:
		#print clientt
		#print topic
		#print delay_time
		#print count
		data = random.randint(30, 40)
		dataToSend = "value=" + str(data)
		print dataToSend
		clientt.publish(topic, dataToSend, 0)
		time.sleep(delay_time)
		count = count - 1
		print count
	clientt.loop_stop()
	clientt.disconnect()

def tmpThrd():
	j = 0
	while j < 10:
		print j
		j = j + 1

	
try:	
	thread.start_new_thread(publishTemp, (client, "/data/from/tesensor1", 3, 20))
	#thread.start_new_thread(tmpThrd, ())
	thread.start_new_thread(publishTemp, (client1, "/data/from/tesensor2", 5, 20))
	thread.start_new_thread(publishTemp, (client2, "/data/from/tesensor3", 2, 20))
	thread.start_new_thread(publishTemp, (client3, "/data/from/tesensor4", 5, 20))
	thread.start_new_thread(publishTemp, (client4, "/data/from/tesensor5", 5, 20))
except:
	print "Error: unable to start thread"

while 1:
	pass
