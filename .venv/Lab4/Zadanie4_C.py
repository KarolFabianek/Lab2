"""Maksymalna prędkość obrotowa w każdej osi w czasie 10 s."""
from mpu6050 import mpu6050
import time

CZAS_POMIARU = 10  # s

sensor = mpu6050(0x68)
maksimum = {"x": 0.0, "y": 0.0, "z": 0.0}

start = time.monotonic()
while time.monotonic() - start < CZAS_POMIARU:
    gyro = sensor.get_gyro_data()
    for os in maksimum:
        maksimum[os] = max(maksimum[os], abs(gyro[os]))
    time.sleep(0.02)

print("Maksymalna predkosc obrotowa:")
for os, wartosc in maksimum.items():
    print(f"{os.upper()}: {wartosc:.1f} deg/s")
