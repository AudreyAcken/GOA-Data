import random, math
from bokeh.plotting import figure, show
import numpy as np

######### Problem Set 6 ##########
#
# Audrey Acken
#
##################################

# 1. Use the vbar (or hbar) glyph and line glyphs to create a box and whisker 
#    function. The arguments are x location for box plot,  and the data as a list.
#    Run 6 sample sets of data and display them on the same figure. Hopefully 
#    you've learned that boxplots mark the 25th, 50th and 75th percentile marks
#    of the data.  Numpy has a function called np.percentile(dataList, percentile).
#    For example np.percentile(data,25) will give the 25th percentile of that data list. 
f = figure()
def boxWhisker(x, data):
  for list in data:
    
    list.sort()
    median1 = len(list)/2
    median2 = len(list)/4
    median3 = 3*median2
    if len(list)%2 == 0:
      median1value = (list[int(median1 - 1)] + list[int(median1)])/2
    else:
      median1value = list[int(median1)]
    if len(list)%4 == 0:
      median2value = (list[int(median2 - 1)] + list[int(median2)])/2
    else:
      median2value = list[int(median2)]
    if len(list)%4 == 0:
      median3value = (list[int(median3 - 1)] + list[int(median3)])/2
    else:
      median3value = list[int(median3)]
    
    f.quad(top=[median2value], bottom=[median3value], left=[x - 0.05], right=[x + 0.05], color="#B3DE69")
    
    xvals = [x - 0.05, x + 0.05]
    yvals = [median1value, median1value]
    f.line(xvals, yvals)
    y = [list[0], list[-1]]
    f.line(x,y)
    show(f)
    x += 0.2
boxWhisker(1, [[1, 2, 3, 4, 5], [5, 7, 8], [3, 4, 5, 9], [10, 7, 4, 6, 9, 3], [1, 1, 1, 4, 3, 10], [2, 7, 5, 3, 6]])
      
'''
# 2. Use the annular_wedge glyph to create a pie chart function.  The arguments should
#    be the x and y location as well as a list of values.  The video here is a full
#    solution.  Feel free to watch it or try it yourself.  I used a few numpy methods
#    however this could also be done without them. It should look like this. (In this
#    video I show you how to add text at the end... don't miss it.)

def pieChart(x, y, listOfData):
  total = sum(listOfData)
  listOfData.insert(0, 0)
  data_array = np.array(listOfData)
  data_angles = data_array*2*math.pi/total
  angles = np.cumsum(data_angles)
  f = figure(x_range = (-1, 3), y_range = (-1, 1))
  for i in range(len(angles)-1):
    wedgeColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    f.annular_wedge(x,y,0,1,angles[i],angles[i+1], color = wedgeColor)
  show(f)
  
pieChart(0, 0, [25, 25, 25, 25])




# 3. Download this filePreview the document on Blood types, taken from 5000 people. 
#    Apparently 38% of the population is type O-Positive whereas only 7% are O-Negative.
#    (Personally I'm O-neg.) Is this consistent with this dataset? 

data = open("bloodTypes.txt", "r")
oPositive = 0
oNegative = 0
counter = 0
for bloodType in data:
  counter += 1
  bloodType = bloodType.strip()
  if bloodType == "O-pos":
    oPositive += 1
  elif bloodType == "O-neg":
    oNegative += 1

print("O-Negative: ", int(oNegative)/counter*100)
print("O-Positive: ", int(oPositive)/counter*100)
print("Yes, this does seem to be consistent with the dataset.")



# 4. Geocontext: Write a function that takes the name of the datafile as an argument. 
#    Then use that function to visualize eight natural structures/monuments on the same
#    set of axes.
#
# Distance (m),Elevation (m)
#
f = figure()
def mapping(files):
  for file in files:
    x = 1
    a = open(file, "r")
    firstLine = True
    col = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 0.2)
    top = []
    bottom = []
    left = []
    right = []
    for line in a:
      line = line.strip()
      data = line.split(",")
      nextX = float(data[0])
      nextY = float(data[1])
      if not firstLine:
        top.append(lastY)
        bottom.append(0)
        left.append(lastX)
        right.append(nextX)
      
      lastX = nextX
      lastY = nextY
      firstLine = False
      x += 1
    #
    minX = min(left)  
    maxX = max(right)
    leftXNormalized = []
    rightXNormalized = []
    for item in left:
      leftXNormalized.append((item - minX) / (maxX - minX))
    for item in right:
      rightXNormalized.append((item - minX) / (maxX - minX))
      
    f.quad(top=top, bottom=bottom, left=leftXNormalized, right=rightXNormalized, color = col)
  show(f)

mapping(["machuPicchu.csv", "victoriaFalls.csv", "grandCanyon.csv", "goldenGate.csv", "mtFuji.csv", "kauai.csv", "halfDome.csv", "niagraFalls.csv"])
     

# 5. Create a simulation using the processing library from a few weeks ago.  Collect 
#    data from that simulation then visualize your results.  The simulation should be 
#    able to collect data without a player.  Remember to watch the videos where I did this.
#    I had to download the processing application in order to make this work at a 
#    reasonable frame rate. Also remember that processing in Trinket only works in Python
#    2, whereas Bokeh is only in Python 3. (Annoying I know.)
#
#    I chose to simulate the pin and ball problem (link to trinket: https://trinket.io/python/30e1f62a86). I then displayed the
#    results in a Histogram:

f = figure()

results = []
data = open("data.csv", "r")
for value in data:
  value = value.strip()
  results.append(int(value))
hist = np.histogram(results, bins = 13, range = (-6, 6))
yVals = hist[0]
xVals = hist[1]
xVals = xVals[0:-1] + 0.5
for (x,y) in zip(xVals, yVals):
  f.vbar(x, 0.8, y, 0)
show(f)

# 6. One of the most fun applications of data science is in sports.  This year, former
#    teammates Lebron James (right) and Kyrie Irving (left) are both potential MVP 
#    contenders for this years NBA season.  One of the most valuable measures is a 
#    statistic called PER (player efficiency rating).  It is a calculation that takes 
#    into account sevaral player statistics, both good and bad.  Take a look at the 
#    equation below.  You might be wondering where those numbers (85.910 and 53.897)
#    come from. Well, the league attempts to force the average PER to be 15 and they 
#    are weighted by importance.  If a player is upwards of 30 for even a few games that
#    is considered to be very good.  Create a list of PER statistics for each player.  
#    Every item in the list should represent a single game.  Then create a box plot 
#    for each player.  Don't forget to add text to the box plot so I know which box 
#    plot belongs with which player. 

# Rk,Place,Opp,Result,MINUTES PLAYED,FGM,FIELD GOAL ATTEMPTS,3PTM,3PA,FREE THROW,FREE THROW ATTEMPTS,OFFENSIVE REB,DEFFENSIVE REB,TRB,ASSISTS,STEALS,BLOCKS,TO,FOULS,PTS
def perCalculation(file):
  Rk = 0
  Place = 1
  Opp = 2
  Result = 3
  MINUTES_PLAYED = 4
  FGM = 5
  FIELD_GOAL_ATTEMPTS = 6
  Three_PTM = 7
  Three_PA = 8
  FREE_THROW = 9
  FREE_THROW_ATTEMPTS = 10
  OFFENSIVE_REB = 11
  DEFFENSIVE_REB = 12
  TRB = 13
  ASSISTS = 14
  STEALS = 15
  BLOCKS = 16
  TO = 17
  FOULS = 18
  PTS = 19

  data = open(file, "r")
  PER = []
  for line in data:
    line = line.strip()
    array = line.split(',')
    if (array[FGM] != ''):
      perValue = ( (float(array[FGM]) * 85.910)
                 + (float(array[STEALS]) * 53.897)
                 + (float(array[Three_PTM]) * 51.757)
                 + (float(array[FREE_THROW_ATTEMPTS]) * 46.845)
                 + (float(array[BLOCKS]) * 39.190)
                 + (float(array[OFFENSIVE_REB]) * 39.190)
                  + (float(array[ASSISTS]) * 34.677)
                 + (float(array[DEFFENSIVE_REB]) * 14.707)
                 - (float(array[FOULS]) * 17.174)
                 - ((float(array[FREE_THROW_ATTEMPTS])-float(array[FREE_THROW])) * 20.091)
                 - ((float(array[FIELD_GOAL_ATTEMPTS]) - float(array[FGM])) * 39.190)
                 - (float(array[TO]) * 53.897))
      PER.append(perValue)
  return PER

# function from earlier:

f = figure()
def boxWhisker(x, data):
  for list in data:
    
    list.sort()
    median1 = len(list)/2
    median2 = len(list)/4
    median3 = 3*median2
    if len(list)%2 == 0:
      median1value = (list[int(median1 - 1)] + list[int(median1)])/2
    else:
      median1value = list[int(median1)]
    if len(list)%4 == 0:
      median2value = (list[int(median2 - 1)] + list[int(median2)])/2
    else:
      median2value = list[int(median2)]
    if len(list)%4 == 0:
      median3value = (list[int(median3 - 1)] + list[int(median3)])/2
    else:
      median3value = list[int(median3)]
    
    f.quad(top=[median2value], bottom=[median3value], left=[x - 0.05], right=[x + 0.05], color="#B3DE69")
    
    xvals = [x - 0.05, x + 0.05]
    yvals = [median1value, median1value]
    f.line(xvals, yvals)
    y = [list[0], list[-1]]
    f.line(x,y)
    show(f)
    x += 0.2
    
    f.text(1, 2250, ["Kyle Irving"])
    f.text(1.2, 3000, ["Lebron James"])

boxWhisker(1, [perCalculation("kyleIrving.csv"), perCalculation("lebronJames.csv")])
'''
  
  



  