from bokeh.plotting import figure, show
import numpy as np
import math

a = open("rankings.csv", "r")

for line in a:
  line = line.strip()
  line = line.split(',')
  c = open("gdp.csv", "r")
  for row in c:
    row = row.strip()
    row = row.split(',')
    e = open("continents.csv", "r")
    for blah in e:
        blah = blah.strip()
        blah = blah.split(',')
        if (row[0] == line[0]) and (row[0] == blah[1]):
          b = open("other.csv", "a")
          b.write(line[1] + "," + row[1] + "\n")


d = open("final.csv", "r")
xVals = []
yVals = []
labels = []
for line in d:
  line = line.strip()
  line = line.split(',')
  if len(line) == 4:
    if line[3] == "Africa":
      labels.append(line[0])
      xVals.append(float(line[1]))
      yVals.append(float(line[2]))

bestFit = np.polyfit(xVals,yVals,1)

yIntercept = bestFit[1]
slopeGood = bestFit[0]
      
f = figure(title="GDP vs. Agricultural Productivity per country", x_axis_label="Agricultural value added per worker", y_axis_label="Gross Domestic Product")

f.circle(xVals, yVals)
f.line([0, 10000], [float(yIntercept), 10000*float(slopeGood)+float(yIntercept)])

for i in range(len(labels)):
  f.text(float(xVals[i])+5, float(yVals[i])+10, [labels[i]], text_font_size = "10pt")

show(f)
'''
#### bar ######

startAngle = 0
x = 1
f = figure(x_range=(-1000,8000),plot_width=700, plot_height=200, y_range=(0,2))
data = {'Southern Africa':3.5, 'South America':10, 'South Asia':29, 'East Asia':41,'North America':12}
for item in data:
  if data[item] == 3.5:
      f.annular_wedge(x+500, 1, 0, 500, startAngle + (startAngle + data[item]*2*math.pi/100), 100-(startAngle + data[item]*2*math.pi/100),color=(128,128,128))
      f.annular_wedge(x+500, 1, 0, 500, startAngle, startAngle + data[item]*2*math.pi/100, color = (255,0,0))
      f.text(x, 1.75, [item], text_font_size = "10pt")
      x += 1500
  else:
    f.annular_wedge(x+500, 1, 0, 500, startAngle + (startAngle + data[item]*2*math.pi/100), 100-(startAngle + data[item]*2*math.pi/100),color=(128,128,128))
    f.annular_wedge(x+500, 1, 0, 500, startAngle, startAngle + data[item]*2*math.pi/100, color = (0,255,0))
    f.text(x, 1.75, [item], text_font_size = "10pt")
    x += 1500
show(f)

a = open("rankings.csv", "r")

for line in a:
  line = line.strip()
  line = line.split(',')
  c = open("poverty.csv", "r")
  for row in c:
    row = row.strip()
    row = row.split(',')
    e = open("continents.csv", "r")
    for blah in e:
        blah = blah.strip()
        blah = blah.split(',')
        if (row[0] == line[0]) and (row[0] == blah[1]):
          #b = open("other.csv", "a")
          #b.write(line[1] + "," + row[1] + "\n")
          b = open("final2.csv", "a")
          b.write(line[0] + "," + line[1] + "," + row[1] + "," + blah[0] + "\n")
          


d = open("final2.csv", "r")
xVals = []
yVals = []
labels = []
for line in d:
  line = line.strip()
  line = line.split(',')
  if len(line) == 4:
    if line[3] == "Africa":
      labels.append(line[0])
      xVals.append(float(line[1]))
      yVals.append(float(line[2]))

bestFit = np.polyfit(xVals,yVals,1)

yIntercept = bestFit[1]
slopeGood = bestFit[0]
      
f = figure(title="% of Population below Poverty line vs. Agricultural Productivity", x_axis_label="Agricultural value added per worker", y_axis_label="Percent of population below Poverty line")

f.circle(xVals, yVals)
f.line([0, 10000], [float(yIntercept), 10000*float(slopeGood)+float(yIntercept)])

for i in range(len(labels)):
  f.text(float(xVals[i])+5, float(yVals[i])+1, [labels[i]], text_font_size = "10pt")

show(f)
'''



  
  
  
  

