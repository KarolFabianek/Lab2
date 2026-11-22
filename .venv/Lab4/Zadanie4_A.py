"""Alarm odległości: BEZPIECZNIE powyżej progu, ALARM w pozostałych przypadkach."""
import time
import board
import busio
import adafruit_vl53l0x

PROG = 300  # mm

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_vl53l0x.VL53L0X(i2c)

while True:
    print("BEZPIECZNIE" if sensor.range > PROG else "ALARM")
    time.sleep(0.2)
