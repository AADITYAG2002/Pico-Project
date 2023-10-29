from machine import Pin

for i in range(29):
    Pin(i,Pin.OUT,value=1)
