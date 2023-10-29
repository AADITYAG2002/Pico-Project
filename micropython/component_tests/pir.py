from machine import Pin, PWM
from utime import sleep

pwm = PWM(Pin(0))

pwm.freq(1000)

while True:
    for duty in range(65025):
        print(pwm)
        pwm.duty_u16(duty)
        sleep(0.0001)
    for duty in range(65025, 0, -1):
        pwm.duty_u16(duty)
        sleep(0.0001)