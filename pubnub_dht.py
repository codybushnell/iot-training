#!/usr/bin/python3
import Adafruit_DHT
import numpy as np
from pubnub import Pubnub
import time

pubnub = Pubnub(publish_key='pub-c-f0255130-06a3-4d8c-8907-b5d341c895ff', subscribe_key='sub-c-d7752268-bd96-11e6-b38f-02ee2ddab7fe')

for i in range(20):

    readings = []
    for i in range(2):
        measurements = Adafruit_DHT.read_retry(11, 4)
        if (measurements[0] is not None) & (measurements[1] is not None):
            readings.append(measurements)

    humidity, temp_C = np.array(readings).T.mean(axis=1).tolist()
    temp_F = ((9/5)*temp_C) + 32

    pubnub.publish('temperature', {'eon': {'temperature_f': temp_F, 'temperature_c': temp_C}})
    pubnub.publish('humidity', {'eon': {'humidity': humidity}})
