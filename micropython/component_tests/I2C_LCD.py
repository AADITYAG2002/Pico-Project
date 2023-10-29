from machine import I2C, Pin
from time import sleep
from lib.pico_i2c_lcd import I2cLcd
from lib.lcd_api import LcdApi

I2C_ADDR = 0x27
total_rows = 2
total_columns = 16

i2c = I2C(0, sda = Pin(0), scl = Pin(1), freq = 400000)
lcd = I2cLcd(i2c, I2C_ADDR, total_rows, total_columns)

smile = bytearray([0x00, 0x00, 0x0A, 0x0A, 0x11, 0x0E, 0x00, 0x00])
eye = bytearray([0x00,0x00,0x00,0x00,0x14,0x14,0x00,0x00])
heart = bytearray([0x00,0x00,0x1B,0x1F,0x1F,0x0E,0x04,0x00])


lcd.custom_char(0, smile)
lcd.putstr("Vanshika,Khyati")
lcd.putstr(" -Aaditya " + chr(0))
