import random, math, numpy
from bokeh.plotting import figure, show
from bokeh.layouts import gridplot


# 1. Write a function that takes the number of times you play and returns 
#    a list of results for the following game. A player rolls 2 dice. 
#    The positive difference between the two dice is the amount of money they 
#    receive. Create a histogram of the results.  

def diceroll(n):
  results = []
  for i in range(n):
    r1 = random.randint(1,6)
    r2 = random.randint(1,6)
    difference = abs(r1 - r2)
    results.append(difference)
  hist = numpy.histogram(results, bins = 6, range = (0, 6))
  yVals = hist[0]
  xVals = hist[1]
  xVals = xVals[0:-1]+(xVals[0]+xVals[1]/2)
  f = figure()
  for (x,y) in zip(xVals, yVals):
    f.vbar(x, 0.95, y, 0)
    show(f)
    
print(diceroll(10))

'''
# 2. Write a function that takes the number of times you play as 
#    an argument and returns a list of results for the following game.
#    In a bowl there is a 3 blue marbles, 2 red marbles, and a black marble.
#    The game costs $1. The rules are, the player draws two marbles (draw one
#    look at it, put it aside, and then draw another).  If they draw two 
#    marbles of the same color they win $2 (meaning if you win they give
#    you your dollar back and an extra dollar.)  If you draw anything else
#    you get nothing.   
#
#    Note: "W" = win, "L" = lose

def marbleGame(n):
  results = []
  for i in range(n):
    marbles = ["b", "b", "b", "r", "r", "l"]
    c1 = random.choice(marbles)
    marbles.remove(c1)
    c2 = random.choice(marbles)
    if c1 == c2:
      results.append("W")
    else:
      results.append("L")
  return results
      

print(marbleGame(20))



# 3. Write a function that takes a list of values and a target value
#    as arguments and returns True if any of the values in the list are
#    above the target value. False otherwise.

x = [1, 2, 3, 4, 5, 6, 7]

def aboveTarget(items, value):
  counter = 0
  for item in items:
    if item > value:
      counter +=1
  if counter > 0:
    return True
  else:
    return False

print(aboveTarget(x, 7))



# 4. Fix My Mistakes!

# Situation 1 - Below is a function that is supposed to count the 
#               number of times counts the amount of times a number
#               above 100 shows up in a list.  Fix my mistake(s). 

def sit1(mylist):
    count = 0
    for item in mylist:
        if item > 100:
            count += 1
    return count

print(sit1([1, 100, 200, 300]))

# Situation 2 - Below is a function that is supposed to return 
#               a list of booleans if a value is between 90 and
#               110 it is True otherwise it's False.  Fix my mistakes(s). 

def sit2(mylist):
    bools = []
    for item in mylist:
      if item > 90 and item < 110:
          bools.append(True)
      else:
          bools.append(False)
    return bools

print(sit2([1, 91, 90, 100]))

# Situation 3 - Below is a function that is supposed to return True 
#               if one of the values in the list is over 100. Fix my mistake(s).

def sit3(mylist):
    found = False
    for item in mylist:
        if item > 100:
            found = True
    return found

print(sit3([101, 90, 80, 200]))

# 5. Roulette is a casino game that involves a steel ball spinner around a
#    wheel. There are 38 slots for the ball to drop. 18 of those slots are
#    colored red, another 18 are colored black and 2 are colored green. If
#    a person bets $1 then the player is expected to win $0.954 per game.
#    Or in other words, if the player played 100 and bet $1 every time they
#    would walk away with approximately $95. Imagine 100 people come in to
#    a casino to play Roulette and they are each going to play 200 times.   
#    Create a line chart and histogram that describes these results. Is this 
#    consistent with what you would expect?
#
#    NOTE: expected win is histogram results / 200


f = figure()

def roulette(players, times):
    playerWins = []
    for i in range(players):
      played = []
      won = []
      amountWon = 0
      for x in range(times):
        played.append(x + 1)
        wheel = random.randint(0, 37)
        if wheel == 0 or wheel == 1:
          wheelColor = "green"
        elif wheel > 18:
          wheelColor = "red"
        else:
          wheelColor = "black"
        
        choice = random.randint(0, 1)
        if choice == 0:
          choiceColor = "red"
        else:
          choiceColor = "black"
        
        if choiceColor == wheelColor:
          amountWon += 2
          
        won.append(amountWon)
      
      playerWins.append(amountWon)

      xVals = played
      yVals = won
      f.line(xVals, yVals, line_width = 2)

    hist = numpy.histogram(playerWins, bins = 2*times, range = (0, 2*times))
    yVals = hist[0]
    xVals = hist[1]
    xVals = xVals[0:-1]+(xVals[0]+xVals[1]/2)
    f1 = figure()
    for (x,y) in zip(xVals, yVals):
      f1.vbar(x, 0.95, y, 0)

    p = gridplot([[f], [f1]])
    show(p)

print(roulette(100, 200))
      
        


# 6. Create two lists of strings, where there are no repeated elements in the
#    individual lists.  Write a function that returns the number of duplicate
#    entries in each list.  For example if we have x = ['a','b','c','d'] and 
#    y = ['a','c','e','f'] the function would return 2 because 'a' and 'c' are
#    in both lists.

def repeats(x, y):
  x.sort()
  y.sort()
  xIndex = 0
  yIndex = 0
  repeats = 0
  while(xIndex < len(x)) and (yIndex < len(y)):
    if x[xIndex] == y[yIndex]:
      repeats += 1
      xIndex += 1
      yIndex += 1
    elif x[xIndex] < y[yIndex]:
      xIndex +=1
    else:
      yIndex += 1
  return repeats

print(repeats([1, 2, 3, 4], [6, 7, 8, 9]))


# 7. Monty Hall Problem

f = figure(title = "Monty Hall Problem", width=1000, height=500)

def montyHall(m, n):
  for i in range(n):
    counter = 0
    total = 0
    yVals = []
    xVals = []
    for x in range(m):
      total += 1
      prize = random.randint(0, 2)
      choice = random.randint(0, 2)
      if prize != choice:
        counter += 1
      xVals.append(total)
      yVals.append(counter/total)
    
    cols = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    f.line(xVals, yVals, color = cols, line_width = 2)
    show(f)
    
print(montyHall(500, 20))
'''     
        
      
    
    
    
      
  
    