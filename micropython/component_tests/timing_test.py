from machine import Pin
import utime

trigger = Pin(0, Pin.OUT)
echo = Pin(1, Pin.IN)

while True:
    trigger.low()
    print("trigger", trigger.value())
    utime.sleep_us(5)
    trigger.high()
    print("trigger", trigger.value())
    utime.sleep_us(5)