from gpiozero import LED, AngularServo
from time import sleep

led = LED(23)
servo = AngularServo(24, min_angle=-90, max_angle=90)


def migaj(czas, ile_razy):
    for _ in range(ile_razy):
        led.on()
        sleep(czas)
        led.off()
        sleep(czas)


while True:
    # ruch w lewo - miganie wolne
    servo.angle = -90
    migaj(1, 2)
    # ruch w prawo - miganie szybkie
    servo.angle = 90
    migaj(0.2, 10)
