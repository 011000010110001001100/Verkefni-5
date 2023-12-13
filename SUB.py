#Helgi Sigurður Júlíusson
#Verkefni 5
#SUBSCRIBER
import time
import machine
import ubinascii
import ujson
from umqtt.simple import MQTTClient

SSID = "123456789"
PASSWORD = "2444666668888888"
BROKER_IP = "https://test.mosquitto.org"
BROKER_PORT = 1883
CLIENT_ID = "Verkefni5.py"

def tengjast_mqtt():
    client = MQTTClient(CLIENT_ID, BROKER_IP, port=BROKER_PORT)
    client.connect()
    print("Tengt við MQTT broker")
    return client

def skrá_sig_á_topic(client, topic):
    client.subscribe(topic)
    print(f"Skráði sig á topic: {topic}")

def fá_mqtt_gögn(topic, msg):
    print(f"Fengin gögn á topic {topic}: {msg}")

def main():
    wlan = machine.WLAN(machine.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)

    while not wlan.isconnected():
        pass
    print("Tengt við WiFi:", wlan.ifconfig())

    mqtt_client = tengjast_mqtt()
    skrá_sig_á_topic(mqtt_client, 'telemetry')

    while True:
        msg = mqtt_client.check_msg()
        if msg is not None:
            fá_mqtt_gögn(msg[0], msg[1])
        
        time.sleep(1)

if __name__ == "__main__":
    main()




