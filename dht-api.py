#!/usr/bin/python3
from flask import Flask, jsonify
import Adafruit_DHT

app = Flask(__name__)

@app.route('/sensor-measurements')
def sensor_measurements():
    
    humidity, temp_C = Adafruit_DHT.read_retry(11, 4)
    temp_F = ((9/5)*temp_C) + 32
    return(jsonify(dict(humidity=humidity, temp_C=temp_C, temp_F=temp_F)))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
