from paho.mqtt import client as mqtt_client
from config import *

def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
 
            print("Failed to connect, return code %d\n", rc)

def connect_mqtt():
    client = mqtt_client.Client(MQTT_CLIENT_ID)
    client.on_connect = on_connect
    client.connect(MQTT_BROKER, MQTT_PORT)
    return client


def publish(client,topic,message):    
    result = client.publish(topic, message)    
    status = result[0]
    if status == 0:
        print(f"Send `{message}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")

def mqtt_pub(message,mqtt_topic):
    client = connect_mqtt()
    # client.loop_start()
    publish(client,message=message,topic=mqtt_topic)

# def mqtt_run():
    
    