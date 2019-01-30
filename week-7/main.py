from processing import *
import math, random, time

'''
# 1. Create a class called Playlist.  To initialize an instance you must 
#    give only a name.  Then create the following methods. 

class Playlist:
  list = []
  def __init__(self, name):
    self.name = name
  
  def add(self, song):
    self.list.append(song)
  
  def addFirst(self, song):
    self.list.insert(0,song)
  
  def swap(self, song1, song2):
    self.list[self.list.index(song1)] = song2
    self.list[self.list.index(song2)] = song1
  
  def moveLast(self, song):
    self.list.remove(song)
    self.list.append(song)
  
  def moveFirst(self, song):
    self.list.remove(song)
    self.list.insert(0, song)
  
  def delete(self, song):
    self.list.remove(song)
  
  def getSongs(self):
    for song in self.list:
      print song
'''
# 2. Let's build up your launcher problem into a game.  Here is my version
#    (Links to an external site.)Links to an external site. of the old launcher
#    problem, you can use this one or yours.  Your game must incorporate these 
#    elements:  Lists, classes, collisions, high score file, timer, points, user 
#    control.   Feel free to add more elements into your game, my version is 
#    the barebones version. 
a = open("highscores.txt", "r")
highScore = 0
for line in a:
  highScore = int(line.strip())
startTime = time.clock()
bulletX = mouseX
bulletY = mouseY
firing = False
yVel = 5
score = 0
timer = 30
list = []
diameter = 20
endGame = False

class targets:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def move(self):
    self.x -= 2

def setup():
  size(1000,800)
  
def draw():
  global bulletX, bulletY, firing, yVel, list, diameter, score, endGame
  if random.randint(1, 50) == 1:
    target = targets(1000, random.randint((0+(diameter/2)), (800-(diameter/2))))
    list.append(target)
  background(200)
  copyList = []
  for item in list:
      item.move()
      ellipse(item.x, item.y, diameter, diameter)
      if item.x > 0:
        copyList.append(item)
  list = copyList
  textSize(30)
  curTime = time.clock()
  elapsedTime = curTime - startTime
  if not endGame:
    text(int(30 - elapsedTime), 10, 70)
    if ((30 - elapsedTime) < 0):
        endGame = True
        if score > highScore:
          b = open("highscores.txt", "a")
          b.write("\n" + str(score))
  else:
    text("Game Over", 50, 200)
  text(score, 10, 30)
  if firing == False:
    bulletX = mouseX + 10
    bulletY = mouseY - 10
  else:
    bulletX += 10
    bulletY -= yVel
    yVel -= .2
    
  if bulletX >= 1020 or bulletY >= 820:
    firing = False
    bulletX = mouseX + 10
    bulletY = mouseY - 10
    yVel = 5
    
  #drawing
  ellipse(bulletX,bulletY,20,20)
  ellipse(mouseX,mouseY,40,40)
  
  for item in list:
    distance = math.sqrt((item.x - bulletX)**2 + (item.y - bulletY)**2)
    if distance < diameter:
      score += 1
      item.x = -100
      
  if score > highScore:
    text("New High Score!", 60, 30)

def mouseClicked():
  global firing, endGame
  if firing == False and endGame == False:
    firing = True
  
run()
'''
# 3. Create balls of random size, color and elasticity. When you hold down the 
#    mouse balls are created during the duration of the time the mouse is being held.
list = []

def setup():
  size(600, 500)

def draw():
  global list
  if mousePressed == True:
    diameter = random.randint(20, 100)
    color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    elasticity = (random.randint(25, 90)/100)
    changeY = 5
    list.append([mouseX, mouseY, diameter, color, elasticity, changeY])
  background(200)
    
  for item in list:
    color = item[3]
    fill(color[0], color[1], color[2])
    item[1] += item[5]
    item[5] += 0.5
    if item[1] > 500-(item[2]/2):
      item[1] = 500-(item[2]/2)
      item[5] *= (-1*item[4])
      if abs(item[5]) < (item[2]/200):
        item[5] = 0
    ellipse(item[0], item[1], item[2], item[2])
      

run()
'''