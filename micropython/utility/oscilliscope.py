from machine import Pin, I2C, PWM, ADC
import utime

#lets go!
button = Pin(10, Pin.IN, Pin.PULL_DOWN)

pwm = PWM(Pin(12))
pwm.freq(100) #1k
pwm.duty_u16(32767)

adc_read = ADC(26) #A read takes 2us therefore 500ks/s!

i2c = I2C(0,sda=Pin(0),scl=Pin(1),freq=40000)

coefficient = 3.35 / 32767

while True:
    reading = adc_read.read_u16()
    calcvoltage = reading * coefficient
    print("V", calcvoltage)
    utime.sleep(0.01)