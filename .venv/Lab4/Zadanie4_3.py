"""Detekcja ruchu na podstawie normy wektora przyspieszenia."""
from mpu6050 import mpu6050
import math
import time

PROG_RUCHU = 12.0  # m/s^2

sensor = mpu6050(0x68)

while True:
    a = sensor.get_accel_data()
    magnitude = math.sqrt(a["x"]**2 + a["y"]**2 + a["z"]**2)

    print(f"Przyspieszenie: {magnitude:.2f}")
    if magnitude > PROG_RUCHU:
        print("WYKRYTO RUCH!")

    time.sleep(0.1)
