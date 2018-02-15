# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import ST7735 as TFT
import Adafruit_GPIO as GPIO
import Adafruit_GPIO.SPI as SPI

from random import randint


WIDTH = 128
HEIGHT = 160
SPEED_HZ = 64000000


# Raspberry Pi configuration.
DC = 24
RST = 25
SPI_PORT = 0
SPI_DEVICE = 0
points=[[15,15,5,50],
        [50,50,10,200]]
points2=[[70,60,20,40],
        [30,80,10,200]]
# BeagleBone Black configuration.
# DC = 'P9_15'
# RST = 'P9_12'
# SPI_PORT = 1
# SPI_DEVICE = 0

# Create TFT LCD display class.
disp = TFT.ST7735(
    DC,
    rst=RST,
    spi=SPI.SpiDev(
        SPI_PORT,
        SPI_DEVICE,
        max_speed_hz=SPEED_HZ))

def randomPointGenerator(num):
    global points2
    points2=[]
    for i in range(num):
        points2.append([randint(0,129),randint(0,161),randint(0,10),randint(0,255)])


# Initialize display.
disp.begin()


disp.clear((255,255,255)) 

# Get a PIL Draw object to start drawing on the display buffer.
draw = disp.draw()

# Draw some shapes.
# Draw a blue ellipse with a green outline.
#draw.ellipse((10, 10, 20, 20),fill=(200,200,200))
for i in range(0,len(points)):

    x1=points[i][0]-points[i][2]
    x2=points[i][0]+points[i][2]
    y1=points[i][1]-points[i][2]
    y2=points[i][1]+points[i][2]
    colour=points[i][3]
    draw.ellipse((x1,y1,x2,y2),fill=(colour,colour,colour))

disp.display()

for x in range(60):

    disp.clear((255,255,255)) 

    # Get a PIL Draw object to start drawing on the display buffer.
    draw = disp.draw()

    for i in range(0,len(points2)):

        x1=points2[i][0]-points2[i][2]
        x2=points2[i][0]+points2[i][2]
        y1=points2[i][1]-points2[i][2]
        y2=points2[i][1]+points2[i][2]
        colour=points2[i][3]
        draw.ellipse((x1,y1,x2,y2),fill=(colour,colour,colour))
    randomPointGenerator(7)

    disp.display()

