import random, math
from bokeh.plotting import figure, show
import numpy as np

data = ["data.csv", "data3.csv", "data4.csv", "data5.csv"]
dataNames = ["Strategy 1", "Strategy 3", "Strategy 4", "Strategy 5"]

f = figure()

initY = 0

for file in data:
  a = open(file, "r")
  results = []
  for line in a:
    line = float(line.strip())
    results.append(line)
  hist = np.histogram(results, bins = 20, range = (0, 100))
  for item in hist[0]:
    item/len(results)
  yVals = hist[0]
  xVals = hist[1]
  xVals = xVals[0:-1]+(xVals[0]+xVals[1]/2)
  for (x,y) in zip(xVals, yVals):
    f.vbar(x, 4.9, y + initY, initY)
  f.text(0, initY - 10, [dataNames[data.index(file)]])
  initY += 100
  
show(f)