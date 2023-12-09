from machine import Pin, SPI
from lib import max7219
from time import sleep

spi = SPI(0,sck=Pin(2),mosi=Pin(3))
cs = Pin(5, Pin.OUT)

display = max7219.Matrix8x8(spi,cs,1)  # (spi, cs, no. of matrices)
display.brightness(1)

def disp_image(image):
    for row in range(8):
        for col in range(8):
            bit = (image[row] >> col) & 0b1
            display.pixel(col,row, bit)

display.fill(0)
display.show()

face = [
    0b00000000,
    0b11100111,
    0b10100101,
    0b11100111,
    0b00000000,
    0b11000011,
    0b00111100,
    0b00000000,
]
face_closed = [
    0b00000000,
    0b00000000,
    0b11100111,
    0b00000000,
    0b00000000,
    0b11000011,
    0b00111100,
    0b00000000,
]

diyas = [
    [
    0b00010000,
    0b00011000,
    0b00011000,
    0b00110000,
    0b00110000,
    0b00011000,
    0b01111110,
    0b00111100,
    ],
    [
    0b00010000,
    0b00011000,
    0b00011000,
    0b00111000,
    0b00111000,
    0b00011000,
    0b01111110,
    0b00111100,
    ],
    [
    0b00010000,
    0b00011000,
    0b00011000,
    0b00111100,
    0b00111100,
    0b00011000,
    0b01111110,
    0b00111100,
    ],
    [
    0b00010000,
    0b00011000,
    0b00011000,
    0b00011100,
    0b00011100,
    0b00011000,
    0b01111110,
    0b00111100,
    ],
    [
    0b00010000,
    0b00011000,
    0b00011000,
    0b00001100,
    0b00001100,
    0b00011000,
    0b01111110,
    0b00111100,
    ],
    [
    0b00000000,
    0b00010000,
    0b00010000,
    0b00011000,
    0b00001100,
    0b00011000,
    0b01111110,
    0b00111100,
    ],
    [
    0b00000000,
    0b00010000,
    0b00010000,
    0b00011000,
    0b00011100,
    0b00011000,
    0b01111110,
    0b00111100,
    ],
    [
    0b00000000,
    0b00010000,
    0b00010000,
    0b00011000,
    0b00111100,
    0b00011000,
    0b01111110,
    0b00111100,
    ],
    [
    0b00000000,
    0b00010000,
    0b00010000,
    0b00011000,
    0b00110000,
    0b00011000,
    0b01111110,
    0b00111100,
    ]
]

# display.pixel(0,0,1)
# display.pixel(1,1,1)
# display.hline(0,4,8,1)
# display.vline(4,0,8,1)
# display.line(0, 0, 3, 8, 1)
# display.rect(1,1,6,6,1)
# display.fill_rect(24,0,1,1,1)

while True:
    for diya in diyas:
        disp_image(diya)
        display.show()
        sleep(0.1)


# scrolling_message = ("Testing")
# length = len(scrolling_message)
# column = (length * 8)

# display.fill(0)
# display.show()
# sleep(1)


# while True:
#     print(scrolling_message)
#     for x in range(32, -column, -1):     
#         display.fill(0)
#         display.text(scrolling_message ,x,0,1)
#         display.show()
#         sleep(0.1)