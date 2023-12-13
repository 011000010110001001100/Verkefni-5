#Helgi Sigurður Júlíusson
#Verkefni 5
#PUBLISHER

# --------------------- WIFI ---------------------

from network import WLAN, STA_IF #net
from time import sleep_ms #tími eða klukka

SSID = "123456789" #net
LYKILORD = "2444666668888888" #net

wifi = WLAN(STA_IF) #net
if not wifi.isconnected():#net
    print(f"Tengist við {	SSID} ...")#net
    wifi.active(True)#net
    wifi.connect(SSID,LYKILORD) #net
    while not wifi.isconnected():#net
        pass
print(f"Tenging við {SSID}, netupplýsingar:", wifi.ifconfig())#net

#------------------MQTT------------------
import time
import board
import busio #hjálpar L2C fjarstýringunni
from adafruit_seesaw.seesaw import Seesaw #L2C controller
from machine import unique_id #unique i
from ubinascii import hexlify #bin data
from umqtt.simple import MQTTClient #mqtt 

MQTT_BROKER = "test.mosquitto.org"#mqtt
CLIENT_ID = "Verkefni5.py"#client á sub eða pub

#------------------KÓÐI FYRIR RAKA------------------
def main():
    i2c_bus = busio.I2C(board.SCL, board.SDA)
    ss = Seesaw(i2c_bus)
    while True:
        raki = ss.hvererrakinn()
        print(f"raki: {raki}")
        rakinn = 100  
        if raki < rakinn:#ef rakinn en er minni en 100 á að vökva
            print("Vökva")
        else:
            print("Ekki vökva.")#ef vökvinn er yfir 100 áttu ekki að vökva
        time.sleep(1)#bíður í 1 sec áður en kóðinn skrifar út hver rakinn er
if __name__ == "__main__":
    main()




