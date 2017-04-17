#!/usr/bin/env python

import sys
import time
import scrollphat
from smallNumbersFont import smallNumbersFont

timeImages = {
    "night": [0, 17, 27, 14, 0],
    "day": [21, 14, 31, 14, 21],
    "evening": [0, 4, 14, 4, 0],
    "morning": [17, 4, 14, 4, 17]
    }

scrollphat.set_brightness(10)

def draw_time_image(image, offset = 0):
    if image not in timeImages:
        for i in range(0, 5):
            scrollphat.set_col(offset, 0)
            offset += 1
    else:
        currentImage = timeImages[image]
        for i in range(0, len(currentImage)):
            scrollphat.set_col(offset, currentImage[i])
            offset += 1
    scrollphat.update()

def set_time_column(timeValue, column):
    timeValueInt = int(timeValue)
    scrollphat.set_col(column, timeValueInt)

def set_time_image(currentTime):
    hour = int(currentTime[:-4])
    if hour >= 6 and hour < 10:
        draw_time_image("morning")
    elif hour >= 10 and hour < 18:
        draw_time_image("day")
    elif hour >= 18 and hour < 22:
        draw_time_image("evening")
    elif hour >= 22 or hour < 6:
        draw_time_image("night")
            

while True:
    try:
        currentTime = time.strftime('%H%M%S')
        columnOffset = 10
        
        for timeTraveller in range(0, 6):
            set_time_column(currentTime[timeTraveller], columnOffset)
            columnOffset -= 1
            
        set_time_image(currentTime)
        
        scrollphat.update()
        time.sleep(0.5)
        
    except KeyboardInterrupt:
        scrollphat.clear()
        sys.exit(-1)
