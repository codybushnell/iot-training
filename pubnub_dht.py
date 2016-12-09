#!/usr/bin/python3
import Adafruit_DHT
from pubnub import Pubnub
import time

pubnub = Pubnub(publish_key='demo', subscribe_key='demo')

while True:

    humidity, temp_C = Adafruit_DHT.read_retry(11, 4)
    temp_F = ((9/5)*temp_C) + 32

    pubnub.publish('temperature', {'eon': {'temperature_f': temp_F, 'temperature_c': temp_C}})
    pubnub.publish('humidity', {'eon': {'humidity': humidity}})
	time.sleep(5)
