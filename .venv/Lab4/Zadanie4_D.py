"""Monitorowanie urządzenia: ALARM przy ruchu i obiekcie bliżej niż próg."""
from mpu6050 import mpu6050
import math
import time
import board
import busio
import adafruit_vl53l0x

PROG_RUCHU = 12.0       # m/s^2
PROG_ODLEGLOSCI = 300   # mm

imu = mpu6050(0x68)
tof = adafruit_vl53l0x.VL53L0X(busio.I2C(board.SCL, board.SDA))

while True:
    a = imu.get_accel_data()
    magnitude = math.sqrt(a["x"]**2 + a["y"]**2 + a["z"]**2)

    if magnitude > PROG_RUCHU and tof.range < PROG_ODLEGLOSCI:
        print("ALARM")
    else:
        print("OK")
    time.sleep(0.1)
