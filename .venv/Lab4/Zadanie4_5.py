"""Detektor zbliżenia z trzema poziomami ostrzeżenia."""
import time
import board
import busio
import adafruit_vl53l0x

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_vl53l0x.VL53L0X(i2c)

while True:
    distance = sensor.range
    if distance < 100:
        print("UWAGA - obiekt bardzo blisko!")
    elif distance < 300:
        print("Obiekt blisko")
    else:
        print("Brak obiektu w poblizu")
    time.sleep(0.2)
