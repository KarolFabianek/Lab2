from gpiozero import AngularServo
from time import sleep

servo = AngularServo(24, min_angle=-90, max_angle=90)
predkosc = 0.05

while True:
    for kat in range(-90, 91):
        servo.angle = kat
        sleep(predkosc)
    for kat in range(90, -91, -1):
        servo.angle = kat
        sleep(predkosc)
