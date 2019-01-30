from processing import *
import math, random

def setup():
  size(500, 500)
  
def pins(diameter, distance, levels):
  x = 250
  y = 100
  for i in range(levels):
    for a in range(i+1):
      ellipse(x, y, diameter, diameter)
      x += distance
    y += distance
    x -= distance*(i+1.5)
  

times = 1000
levels = 12
diameter = 8
distance = 4*diameter;
x1 = 250
y1 = 50
xChange = 0
yChange = diameter / 2
yPerLevel = int(distance/yChange)
yLevelCount = 0
yLevelComplete = 0 

results = open("data.csv", "w")

def draw():
  global times, levels, x1, y1, yChange, xChange, diameter, distance 
  global yLevelCount, yLevelComplete
  background(255)
  pins(diameter, distance, levels)
  ellipse(x1, y1, 20, 20)
  x1 += xChange
  y1 += yChange
  yLevelCount += 1
  if (yLevelCount == yPerLevel):
    yLevelCount = 0
    yLevelComplete += 1
    choice = random.randint(0, 1)
    if choice == 0:
      xChange = 0 - yChange/2
    else:
      xChange = yChange/2
    
    if (yLevelComplete == levels):    
      bin = int((x1 - 250)/(4*diameter))
      results.write(str(bin) + "\n")
      x1 = 250
      y1 = 100
      yLevelComplete = 0
      xChange = 0
      times -= 1
      if times == 0:
        exit()

run()