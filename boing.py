import scrollphat
import random
import math
import sys
import time

COUNT = 217
MAXBALLS = 10
DELAY = 0.02
BRIGHTNESS = 15

def boundaries(point):
  if point[0] < 0:
    point[0] = 0
    point[2] = -point[2]
  if point[1] < 0:
    point[1] = 0
    point[3] = -point[3] 
  if int(point[0]) > 10:
    point[0] = 10
    point[2] = -point[2]
  if int(point[1]) > 4:
    point[1] = 4
    point[3] = -point[3]

def move(point):
  point[4] = point[0]
  point[5] = point[1]
  point[0] += point[2]
  point[1] += point[3]

def random_point(x,y):
#  x = random.randint(0,10)
#  y = random.randint(0,4)
  dx = random.randint(1,10) * 0.1
  dy = random.randint(1,10) * 0.1
  return [x,y,dx,dy,x,y]
 
def clear_tails(pts):
  for pt in pts:
    scrollphat.set_pixel(int(pt[4]),int(pt[5]),0)

def clear_points(pts):
  for pt in pts:
    scrollphat.set_pixel(int(pt[0]),int(pt[1]),0)
    scrollphat.set_pixel(int(pt[4]),int(pt[5]),0)

def draw_points(pts):
  for pt in pts:
    scrollphat.set_pixel(int(pt[0]),int(pt[1]),1)
    scrollphat.set_pixel(int(pt[4]),int(pt[5]),1)
  
scrollphat.set_brightness(BRIGHTNESS)

count = COUNT
points = [random_point(0,0)]

while True:
  clear_tails(points)
  
  if count < 0:
    count = COUNT
    if len(points) < MAXBALLS:
      points += [random_point(points[0][0],points[0][1])]
    else:
      p = points[MAXBALLS - 1]
      clear_points(points)
      points = [p]

  for point in points:
    move(point)
    boundaries(point)

  draw_points(points)

  scrollphat.update()
  time.sleep(DELAY)
  count -= 1
