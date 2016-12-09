#!/usr/bin/python3
from flask import Flask, Response, jsonify, request
import json
import Adafruit_DHT
import numpy as np

app = Flask(__name__)

@app.route('/sensor-measurements')
def sensor_measurements():
    readings = []
    for i in range(int(request.args.get('samples'))):
        measurements = Adafruit_DHT.read_retry(11, 4)
        if (measurements[0] is not None) & (measurements[1] is not None):
            readings.append(measurements)
    
    humidity, temp_C = np.array(readings).T.mean(axis=1).tolist()
    temp_F = ((9/5)*temp_C) + 32
    return(jsonify(dict(humidity=humidity, temp_C=temp_C, temp_F=temp_F)))

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5555)
