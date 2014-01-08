#!/usr/bin/env python

# SSD1306 PIL (Python Imaging Library) Example
# Please check out: http://www.pythonware.com/products/pil

from PIL import Image, ImageDraw, ImageFont
import pyssd1306 as oled
from time import sleep

I2C_BUS = "/dev/i2c-3"
WHITE = 1
BLACK = 0
W = 128
H = 64

oled.init(I2C_BUS, W, H)
image = Image.new("1", (W, H), BLACK)
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('verdana.ttf', 11)
draw.text((0, 0), 'HELLO, WORLD', font = font)
string = ''.join(map(chr, image.getdata()))
oled.blit(string)

