from processing import *
import math, random, time

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def distance(self, point2):
    return math.sqrt((point2.x-self.x)**2 + (point2.y-self.y)**2)
  
  def move(self, vector1):
    self.x += vector1.h
    self.y += vector1.v
  
  def makeVectorTo(self, point2):
    newVector = Vector(point2.x - self.x, point2.y - self.y)
    return newVector
    

class Vector:
  def __init__(self, h, v):
    self.h = h
    self.v = v
  
  def add(self, vector2):
    self.h += vector2.h
    self.v += vector2.v
  
  def subtract(self, vector2):
    self.h -= vector2.h
    self.v -= vector2.v
  
  def multiply(self, num):
    self.h *= num
    self.v *= num
  
  def divide(self, num):
    if num == 0:
      return "error"
    else:
      self.h = self.h/num
      self.v = self.v/num
  
  def length(self):
    return math.sqrt((self.h**2) + (self.v**2))
  
  def normalize(self):
    self.h = self.h/self.length()
    self.v = self.v/self.length()
    
  def random(self, length):
    self.h = random.random() * length
    self.v = math.sqrt(4-(self.h**2))

class Circle:
  def __init__(self):
    self.position = Point(random.randint(4, 796), random.randint(4, 596))
    self.vector = Vector(0, 0)
    self.vector.random(2)
    self.virus = 0
    self.hasTarget = False
    self.counter = 0
  
  def makeVirus(self):
    global strategy
    self.virus = 1
    if strategy == 2:
      self.vector = Vector(0, 0)
    if strategy == 3:
      self.vector = Vector(0, 0)
      self.vector.random(2)
  
  def draw(self):
    if self.virus == 0:
      fill(0, 255, 0)
    else:
      fill(255, 0, 0)
    ellipse(self.position.x, self.position.y, 7, 7)
    self.position.move(self.vector)
    if self.position.x <= 3.5 or self.position.x >= 796.5:
      self.vector.h *= -1
    if self.position.y <= 3.5 or self.position.y >= 596.5:
      self.vector.v *= -1
  def distance(self, circle):
    return self.position.distance(circle.position)

circles = []
viruses = []

def updates():
  global circles, viruses
  updatedCircles = []
  updatedViruses = viruses
  for circle in circles:
    if circle.virus == 1:
      updatedViruses.append(circle)
    else:
      updatedCircles.append(circle)
  circles = updatedCircles;
  viruses = updatedViruses

# Strategy 1: Completely Random
def strategy1():
  global circles, viruses
  for virus in viruses:
    for circle in circles:
      if virus.distance(circle) < 7:
        circle.makeVirus()

# Strategy 2: Still unless within 50 pixels
def strategy2():
  global circles, viruses
  for virus in viruses:
    if virus.hasTarget == False:
      for circle in circles:
        if virus.distance(circle) <= 50:
          virus.hasTarget = True
          virus.target = circle
    else:
      if virus.target.virus == 1:
        virus.hasTarget = False
        virus.vector = Vector(0, 0)
      else:
        virus.vector = virus.position.makeVectorTo(virus.target.position)
        virus.vector.normalize()
        virus.vector.multiply(2)
          
    for circle in circles:      
      if virus.distance(circle) < 7:
        circle.makeVirus()
        virus.hasTarget = False
        virus.vector = Vector(0, 0)

# Strategy 3: Random unless within 50 pixels
def strategy3():
  global circles, viruses
  for virus in viruses:
    if virus.hasTarget == False:
      for circle in circles:
        if virus.distance(circle) <= 50:
          virus.hasTarget = True
          virus.target = circle
    else:
      if virus.target.virus == 1:
        virus.hasTarget = False
      else:
        virus.vector = virus.position.makeVectorTo(virus.target.position)
        virus.vector.normalize()
        virus.vector.multiply(2)
          
    for circle in circles:      
      if virus.distance(circle) < 7:
        circle.makeVirus()
        virus.hasTarget = False

# Strategy 4: Viruses repel each other       
def strategy4():
  global circles, viruses
  for virus in viruses:
    for circle in circles:
      if virus.distance(circle) < 7:
        circle.makeVirus()
    for virus2 in viruses:
      if virus2 != virus:
        if virus.distance(virus2) < 14 and virus.counter == 0:
          virus.vector.multiply(-1)
          virus.counter = 20
    if virus.counter > 0:
      virus.counter -= 1

# Strategy 5: Viruses form line(s)
def strategy5():
  global circles, viruses
  for virus in viruses:
    for virus2 in viruses:
      if virus2 != virus:
        if virus.distance(virus2) < 14:
          virus2.vector = virus.vector
          virus2.position.x = virus.position.x
          virus2.position.y = virus.position.y + 14

    for circle in circles:
      if virus.distance(circle) < 7:
        circle.makeVirus()
          
def initCircles():
  global circles, viruses, startTime
  circles = []
  viruses = []
  for i in range(50):
    circles.append(Circle())
  viruses.append(Circle())
  viruses[0].makeVirus()
  startTime = time.clock()
  
def setup():
  size(800,600)
  initCircles()
  
def draw():
  global circles,trials, max_trials, startTime, strategy
  if (trials < max_trials):
    background(200)
    for circle in circles:
      circle.draw()
    for virus in viruses:
      virus.draw()


    if strategy == 1:
      strategy1()
      if (len(circles) == 0):
        trials += 1
        elapsed = time.clock() - startTime
        a = open("data1.csv", "a")
        a.write(str(elapsed) + "\n")
        initCircles()
  
    elif strategy == 2:
      strategy2()
      elapsed = time.clock() - startTime
      if elapsed > 60:
        initCircles()
      else:
        if (len(circles) == 0):
          trials += 1
          a = open("data2.csv", "a")
          a.write(str(elapsed) + "\n")
          initCircles()
          
    elif strategy == 3:
      strategy3()
      if (len(circles) == 0):
        trials += 1
        elapsed = time.clock() - startTime
        a = open("data3.csv", "a")
        a.write(str(elapsed) + "\n")
        initCircles()
    elif strategy == 4:
      strategy4()
      if (len(circles) == 0):
        trials += 1
        elapsed = time.clock() - startTime
        a = open("data4.csv", "a")
        a.write(str(elapsed) + "\n")
        initCircles()
    
    elif strategy == 5:
      strategy5()
      if (len(circles) == 0):
        trials += 1
        elapsed = time.clock() - startTime
        a = open("data4.csv", "a")
        a.write(str(elapsed) + "\n")
        initCircles()
    
    updates()

max_trials = 100
trials = 0

##### Change Strategy Number Below: ######
strategy = 4
run()
