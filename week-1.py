from processing import *
import math, random


# 1. Make a ball such that when you hold down the mouse the ball's 
# radius grows. Add the feature that when the radius is above
# 150 it starts to shrink and if the radius is smaller than 10 
# it begins to grow again.

diameter = 10
grow = True

def setup():
  size(500, 500)

def draw():
  global diameter, grow
  background(225)
  if mousePressed:
    if grow == True:
      diameter += 3
      if diameter > 150:
        grow = False
    else:
      diameter -= 3
      if diameter < 10:
        grow = True
      
    
  ellipse(250, 250, diameter, diameter)

run()

'''

# 2. Make the ball jump to the location of the mouse when you click
x = 250
y = 250

def setup():
  size(500, 500)

def draw():
  background(225)
  ellipse(x, y, 20, 20)

def mousePressed():
  global x, y
  x = mouseX
  y = mouseY
  
run()


# 3. Create two circles. One of the circle is attracted to your mouse 
# and always moves towards it whereas the other circle always moves away from it.

x1 = random.randint(15, 500-15)
x2 = random.randint(15, 500-15)
y1 = random.randint(15, 500-15)
y2 = random.randint(15, 500-15)

def setup():
  size(500, 500)

def draw():
  global x1, x2, y1, y2
  x1change = (mouseX - x1)/100
  y1change = (mouseY - y1)/100
  x2change = (mouseX - x2)/100
  y2change = (mouseY - y2)/100
  background(225)
  ellipse(x1, y1, 30, 30)
  ellipse(x2, y2, 30, 30)
  x1 += x1change
  y1 += y1change
  x2 -= x2change
  y2 -= y2change
  if x2 < 15:
    x2 = 15
  elif x2 > 500 - 15:
    x2 = 500 - 15
  if y2 < 15:
    y2 = 15
  elif y2 > 500 - 15:
    y2 = 500 - 15

run()

# 4. Collision: Make two circles that are moving around the screen and bouncing off the
# edges of the window.  If they collide one of them (or both) goes to a random location.

x1 = random.randint(15, 500-15)
x2 = random.randint(15, 500-15)
y1 = random.randint(15, 500-15)
y2 = random.randint(15, 500-15)

y1change = 5
x1change = 5
y2change = 5
x2change = 5

def setup():
  size(500, 500)

def draw():
  global x1, x2, y1, y2, y1change, x1change, y2change, x2change
  background(225)
  ellipse(x1, y1, 30, 30)
  ellipse(x2, y2, 30, 30)
  x1 += x1change
  x2 += x2change
  y1 += y1change
  y2 += y2change
  if x1 > 500-15 or x1 < 15:
    x1change *= -1
  if x2 > 500-15 or x2 < 15:
    x2change *= -1
  if y1 > 500-15 or y1 < 15:
    y1change *= -1
  if y2 > 500-15 or y2 < 15:
    y2change *= -1
  
  distance = math.sqrt(((x1 - x2)**2)+((y1 - y2)**2))
  if distance < 30:
    x1 = random.randint(15, 500-15)
    y1 = random.randint(15, 500-15)
  
run()

# 5. Trigonometry Required. Make the ball circle around your mouse.
angle = 0
def setup():
  size(500, 500)

def draw():
  global angle
  background(225)
  angle += 0.1
  y = mouseY + 100*math.cos(angle)
  x = mouseX + 100*math.sin(angle)
  ellipse(x, y, 30, 30)

run()


# 6. Make a bullet fire from an object and return to that object when it's off the screen. 
x = 70
y = 250
firing = False

def setup():
  size(500, 500)

def draw():
  global x, y, firing
  background(225)
  ellipse(x, y, 10, 10)
  ellipse(50, 250, 40, 40)
  if firing == True:
    x += 5
  if x > 510:
    firing = False
    x = 70
    y = 250
    
  
def mousePressed():
  global firing
  background(225)
  firing = True
  
run()


# 7. Make gravity!  Create a floor, place the ball on the floor then when you push space bar
# the ball flies up and drops down to the floor.  (Make sure it works more than once too.
# And also make sure you can't jump in mid-air.) 
x = mouseX
y = 400-15
yChange = 0
def setup():
  size(500, 500)

def draw():
  global x, y, yChange
  background(225)
  rect(0, 400, 499, 100)
  ellipse(x, y, 30, 30)
  y += yChange
  yChange += 0.5
  if y > 400-15:
    y = 400-15
    yChange = 0

def mousePressed():
  global y, yChange
  yChange = -15

  
run()

# 8. Collision with a box in the middle of the screen. (Conceptually this isn't too difficult 
# but to make a good one is kinda hard.)
x = random.randint(0, 100)
y = random.randint(0, 100)
ySpeed = 5
xSpeed = 5
diameter = 30
radius = diameter/2

def setup():
  size(500, 500)
  
def draw():
  global x, y, xSpeed, ySpeed
  background(225)
  ellipse(x, y, diameter, diameter)
  rect(200, 200, 100, 100)
  if (x + radius) < 200:
    if (y + radius) < 200:
      corner = 0
    elif (y - radius) > 300:
      corner = 6
    else:
      corner = 3
  elif (x - radius) > 300:
    if (y + radius) < 200:
      corner = 2
    elif (y - radius) > 300:
      corner = 8
    else:
      corner = 5
  else:
    if (y + radius) < 200:
      corner = 1
    elif (y - radius) > 300:
      corner = 7
    else:
      corner = 4
    
  x += xSpeed
  y += ySpeed
  if y > 470 or y < 0:
    ySpeed *= -1
  if x > 470 or x < 0:
    xSpeed *= -1
  if (x + radius) > 200 and (x - radius) < 300 and (y + radius) > 200 and (y - radius) < 300:
    if corner == 0 or corner == 2 or corner == 6 or corner == 8:
      ySpeed *= -1
      xSpeed *= -1
    elif (corner == 1 or corner == 7):
      ySpeed *= -1
    elif (corner == 3 or corner == 5):
      xSpeed *= -1
    else:
      ySpeed *= -1
      xSpeed *= -1
  
run()

# 9. Launcher

x = mouseX
y = mouseY
showing = False
yChange = 1

def setup():
  size(1000, 1000)

def draw():
  global x, y, showing, yChange
  background(225)
  if showing == True:
    ellipse(x, y, 10, 10)
    x += 10
    y += yChange
    yChange += 0.5
  else:
    ellipse(mouseX + 9, mouseY - 11, 10, 10)
  ellipse(mouseX, mouseY, 30, 30)
  if (y > 1000) or (x > 1000):
    showing = False
    
  
def mousePressed(): 
  global showing, x, y, yChange
  if (showing == False):
    showing = True
    x = mouseX
    y = mouseY
    yChange = -10
  
run()

# 10. Colliding Balls. 

radius = 30

x1 = random.randint(radius, 500-radius)
x2 = random.randint(radius, 500-radius)
y1 = random.randint(radius, 500-radius)
y2 = random.randint(radius, 500-radius)
y3 = random.randint(radius, 500-radius)
x3 = random.randint(radius, 500-radius)

y1change = 2
x1change = 2
y2change = 3
x2change = 3
y3change = 5
x3change = 5

def setup():
  size(500, 500)

def draw():
  global x1, x2, y1, y2, y1change, x1change, y2change, x2change, x3, y3, x3change, y3change, radius
  background(225)
  ellipse(x1, y1, 2*radius, 2*radius)
  ellipse(x2, y2, 2*radius, 2*radius)
  ellipse(x3, y3, 2*radius, 2*radius)
  x1 += x1change
  x2 += x2change
  y1 += y1change
  y2 += y2change
  x3 += x3change
  y3 += y3change
  if x1 > 500-radius or x1 < radius:
    x1change *= -1
  if x2 > 500-radius or x2 < radius:
    x2change *= -1
  if y1 > 500-radius or y1 < radius:
    y1change *= -1
  if y2 > 500-radius or y2 < radius:
    y2change *= -1
  if y3 > 500-radius or y3 < radius:
    y3change *= -1
  if x3 > 500-radius or x3 < radius:
    x3change *= -1
  
  distance1 = math.sqrt(((x1 - x2)**2)+((y1 - y2)**2))
  if distance1 < 2*radius:
    if x1change * x2change < 0:
      x1change *= -1
      x2change *= -1
    if y1change * y2change < 0:
      y1change *= -1
      y2change *= -1
    
  distance2 = math.sqrt(((x2 - x3)**2)+((y2 - y3)**2))
  if distance2 < 2*radius:
    if x2change * x3change < 0:
      x2change *= -1
      x3change *= -1
    if y2change * y3change < 0:
      y2change *= -1
      y3change *= -1
  
  distance3 = math.sqrt(((x3 - x1)**2)+((y3 - y1)**2))
  if distance3 < 2*radius:
    if x3change * x1change < 0:
      x3change *= -1
      x1change *= -1
    if y3change * y1change < 0:
      y3change *= -1
      y1change *= -1
  
run()
'''


