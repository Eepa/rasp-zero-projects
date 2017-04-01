import scrollphat
import random
import math
import sys
import time

COUNT = 250
MAXBALLS = 5

def boundaries(point):
  if point[0] < 0:
    point[0] = 0
    point[2] = 1
  if point[1] < 0:
    point[1] = 0
    point[3] = 1
  if point[0] > 10:
    point[0] = 10
    point[2] = -1
  if point[1] > 4:
    point[1] = 4
    point[3] = -1

def move(point):
  point[4] = point[0]
  point[5] = point[1]
  point[0] += point[2]
  point[1] += point[3]

def random_point():
  x = random.randint(0,10)
  y = random.randint(0,4)
  return [x,y,1,1,x,y]
 
  
scrollphat.set_brightness(20)

count = COUNT
points = [random_point()]

while True:
  try:
      for point in points:
        scrollphat.set_pixel(point[4],point[5],0)
  
      if count < 0:
        count = COUNT
        if len(points) < MAXBALLS:
          points += [random_point()]
        else:
          p = points[0]
          for point in points:
            scrollphat.set_pixel(point[0], point[1], 0)
          points = [p]

      for point in points:
        move(point)
        boundaries(point)

      for point in points:
        scrollphat.set_pixel(point[0],point[1],1)

      scrollphat.update()
      time.sleep(0.02)
      count -= 1

  except KeyboardInterrupt:
      scrollphat.clear()
      sys.exit(-1)
