#!/usr/bin/python3
import Adafruit_DHT
	
while True:
	humidity, temp_C = Adafruit_DHT.read_retry(11, 4)
	temp_F = ((9/5)*temp_C) + 32
	print("Temperature (F): {}\nTemperature (C): {}\nHumidity (%): {}".format(temp_F, temp_C, humidity))