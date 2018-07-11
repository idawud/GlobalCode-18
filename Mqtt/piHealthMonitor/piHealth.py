from monitor import data
import paho.mqtt.client as mqtt

health = data()
#print(health)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("UCC/pihealth")
    
def on_message(client, userdata, msg):
    print("Message Received: "+" "+str(msg.payload))
    
def on_publish(client, userdata, mid):
    #logging.debug("pub ack "+ str(mid))
    client.mid_value=mid
    client.puback_flag=False

client = mqtt.Client(client_id="23")
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish

client.connect("82.165.16.151", 1883, 60)
client.loop_start()
client.publish("UCC/pihealth","dawud@raspberrypi: " + str(health))
print("Data Sent")