#############################################################################
#
# Week 10 Problem Set
#
# Audrey Acken
#
############################################################################
from bokeh.plotting import figure, show
import numpy as np
import math, random
f = figure()

# 1. Create a dictionary that has the year as a key and the value is how many
#    movies were made that year.   Create an appropriate visual using Bokeh to
#    illustrate this this data. 
'''
a = open("movies.txt", "r")
years = {}
for line in a:
  line = line.strip()
  line = line.split('|')
  key = line[1]
  if key not in years:
    years[key] = 1
  else:
    years[key] += 1

xvals = []
yvals = []
years_sort = [(k, years[k]) for k in sorted(years, key=years.get, reverse = True)]

for item in years_sort:
  f.vbar(int(item[0]), 0.8, item[1], 0)

show(f)
'''


# 2. Determine the actors that have been in the most movies. Create an 
#    appropriate visual using Bokeh to illustrate this this data. 

b = open("movies.txt", "r")
actors = {}
for line in b:
  line = line.strip()
  line = line.split('|')
  movieActors = line[3]
  movieActors = movieActors.split(",")
  for item in movieActors:
    if item != "":
      key = item
      if key not in actors:
        actors[key] = 1
      else:
        actors[key] += 1
  
actors_sort = [(k, actors[k]) for k in sorted(actors, key=actors.get, reverse = True)]

xVals = []
yVals = []
for i in range(0,9):
    xVals.append(actors_sort[i][0])
    yVals.append(actors_sort[i][1])
f = figure(x_range=xVals, title="Actors", toolbar_location=None, tools="")
f.vbar(x=xVals, top=yVals, width=0.9)
f.xaxis.major_label_orientation = 1.4
show(f)


'''
# 3. Determine which director and actor have worked with each other the
#    most. Create an appropriate visual using Bokeh to illustrate this this data.
c = open("movies.txt", "r")
combination = {}
for line in c:
  line = line.strip()
  line = line.split('|')
  movieDirectors = line[2]
  movieDirectors = movieDirectors.split(",")
  movieActors = line[3]
  movieActors = movieActors.split(",")
  for director in movieDirectors:
    for actor in movieActors:
      if actor != "" and director != "":
        key = director + " + " + actor
        if key not in combination:
          combination[key] = 1
        else:
          combination[key] += 1

combination_sort = [(k, combination[k]) for k in sorted(combination, key=combination.get, reverse = True)]


xVals = []
yVals = []
for i in range(0,9):
    xVals.append(combination_sort[i][0])
    yVals.append(combination_sort[i][1])
f = figure(x_range=xVals, title="Director and Actor", toolbar_location=None, tools="")
f.vbar(x=xVals, top=yVals, width=0.9)
f.xaxis.major_label_orientation = 1.4
show(f)
'''

'''
# 4. Create a dictionary where the key is the decade ("1970s") and the value is
#    how many Horror movies were created during that decade. 
d = open("movies.txt", "r")
horror = {}
totalHorror = 0
for line in d:
  line = line.strip()
  line = line.split('|')
  key = str(math.floor(int(line[1])/10)*10) + "s"
  if line[4] == "Horror":
    if key not in horror:
      horror[key] = 1
    else:
      horror[key] += 1
    totalHorror += 1
      
horror_sort = [(k, horror[k]) for k in sorted(horror, key=horror.get, reverse = True)]

filmDegree = 2*math.pi/totalHorror
startAngle = 0

for item in horror_sort:
  randColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
  f.annular_wedge(1, 1, 0, 1, startAngle, startAngle + filmDegree*item[1], color = randColor, legend = item[0])
  startAngle += filmDegree*item[1]
show(f)
'''

# 5. Which pairs of actors have been in the most movies together? Create an 
#    appropriate visual using Bokeh to illustrate this this data.  
'''
e = open("movies.txt", "r")
pairs = {}
for line in e:
  line = line.strip()
  line = line.split('|')
  movieActors = line[3]
  movieActors = movieActors.split(",")
  for actor1 in movieActors:
    for actor2 in movieActors:
      if actor1 != "" and actor2 != "" and actor1 != actor2 and actor1 < actor2:
        key = actor1 + "+" + actor2
        if key not in pairs:
          pairs[key] = 1
        else:
          pairs[key] += 1

pairs_sort = [(k, pairs[k]) for k in sorted(pairs, key=pairs.get, reverse = True)]

xVals = []
yVals = []
for i in range(0,9):
    xVals.append(pairs_sort[i][0])
    yVals.append(pairs_sort[i][1])
f = figure(x_range=xVals, title="Pairs of Actors", toolbar_location=None, tools="")
f.vbar(x=xVals, top=yVals, width=0.9)
f.xaxis.major_label_orientation = 1.4
show(f)
'''
