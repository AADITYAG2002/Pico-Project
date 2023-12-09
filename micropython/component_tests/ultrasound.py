from machine import Pin, I2C
import utime
from lib.pico_i2c_lcd import I2cLcd

trigger = Pin(0, Pin.OUT)
echo = Pin(1, Pin.IN, Pin.PULL_DOWN)

I2C_ADDR = 0x27
total_rows = 2
total_columns = 16

i2c = I2C(0, sda = Pin(4), scl = Pin(5), freq = 400000)
lcd = I2cLcd(i2c, I2C_ADDR, total_rows, total_columns)

def ultrasonic():
    timepassed = 0
    
    # generate trigger pulse
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(10)
    trigger.low()

    #receive echo

    while echo.value() == 0 :
        signaloff = utime.ticks_us()


    while echo.value() == 1 :
        signalon = utime.ticks_us()
    
    timepassed = signalon - signaloff

    return timepassed

while True:
    print('\n')
    print("====== NEW READING =======")
    measured_time = ultrasonic()
    distance_cm = (measured_time * 0.0343) / 2
    print(f"distance : {distance_cm} cm")
    
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr("distance : ")
    lcd.move_to(0,1)
    lcd.putstr(f"{distance_cm} cm")
    
    utime.sleep(0.5)