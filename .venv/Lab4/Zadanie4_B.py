"""Klasyfikacja odległości do trzech stref."""
import time
import board
import busio
import adafruit_vl53l0x

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_vl53l0x.VL53L0X(i2c)

while True:
    distance = sensor.range
    if distance > 500:
        print("DALEKO")
    elif distance >= 200:
        print("BLISKO")
    else:
        print("ALARM")
    time.sleep(0.2)
