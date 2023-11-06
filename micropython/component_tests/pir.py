from machine import Pin
from utime import sleep

pir = Pin(0, Pin.IN, Pin.PULL_UP)
led = Pin('LED', Pin.OUT)
sleep(3)

while True:
    print("pir value : {}".format(pir.value()))
    sleep(0.5)