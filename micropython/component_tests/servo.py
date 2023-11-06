from machine import Pin, PWM
import utime

servo = PWM(Pin(0))
servo.freq(50)

for _ in range(2):
    servo.duty_u16(32767)
    utime.sleep(2)
    servo.duty_u16(2000)
    utime.sleep(2)