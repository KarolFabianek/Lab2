"""Odczyt akcelerometru i żyroskopu MPU-6050."""
from mpu6050 import mpu6050
import time

sensor = mpu6050(0x68)

while True:
    accel = sensor.get_accel_data()
    gyro = sensor.get_gyro_data()

    print("Akcelerometr [m/s^2]:")
    print(f"X = {accel['x']:.2f}")
    print(f"Y = {accel['y']:.2f}")
    print(f"Z = {accel['z']:.2f}")

    print("Zyroskop [deg/s]:")
    print(f"X = {gyro['x']:.2f}")
    print(f"Y = {gyro['y']:.2f}")
    print(f"Z = {gyro['z']:.2f}")

    print("----------------")
    time.sleep(0.5)
