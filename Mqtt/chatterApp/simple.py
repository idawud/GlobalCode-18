import paho.mqtt.client as mqtt
import time

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("Group4/dawud")
    

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("Message Received: "+" "+str(msg.payload))

# The callback for when the client publishes to a channel
def on_publish(client, userdata, mid):
    #logging.debug("pub ack "+ str(mid))
    client.mid_value=mid
    client.puback_flag=False

client = mqtt.Client(client_id="23")
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish

client.connect("82.165.16.151", 1883, 60)

user = input("Enter your Username: ")
while True:
    client.loop_start()
    time.sleep(1)
    message = input("Enter your Message: ")
    client.publish("Group4/dawud", user+ ": " +message)
    #time.sleep(1)
    
client.loop_forever()