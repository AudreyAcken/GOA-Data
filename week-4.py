############################ 2c Practice Problems ############################
#
# Audrey Acken
#
##############################################################################
import math
import random

# Write a function that takes two numbers (floats or integers) as arguments and 
# returns the sum of those two numbers.

def sum(num1, num2):
  return num1 + num2

print("1.", sum(2, -1))

# Write a function that takes one number as an argument and returns the square of
# that number.

def square(num):
  return num**2
  
print("2.", square(12))

# Write a function that uses the previous function and returns the area of a circle. 

def areaOfCircle(radius):
  return math.pi*square(radius)
  
print("3.", areaOfCircle(2))

# Write a function that takes two arguments, one is the bill and the other is the 
# percentage tip you would like to leave. The function should return the total for 
# the bill.

def totalBill(bill, percentTip):
  return bill + (percentTip*bill)

print("4.", totalBill(1, 0.5))

# Write a Python function that computes the cost of a road trip, given the distance
# traveled, the fuel efficiency of the car (in miles per gallon), and the cost of a 
# gallon of gas.

def roadTripCost(distanceTraveled, milesPerGallon, gallonCost):
  return (distanceTraveled/milesPerGallon)*gallonCost

print("5.", roadTripCost(20, 5, 1))

# As part of your community service project, you organize a raffle to raise money for
# a good cause. Tickets cost $5 each and you spent $50 on the prizes.  Write a Python
# function that computes the amount of money you raised.  What arguments do you need?
#
# Arguments:
#    tickets : amount of tickets sold
#    prizes : amount of prizes bought

def moneyRaised(tickets, prizes):
  return (tickets*5) - (prizes*50)

print("6.", moneyRaised(11, 1))

# Write a Python function that computes the monthly payments needed for a 30 year
#mortgage, given the annual interest rate and the amount of money borrowed.
#
# Formula found from https://www.mtgprofessor.com/formulas.htm
#
# Arguments:
#    money : loan amount
#    interestRate : annual interest rate
# Return value:
#    monthly payment for 30 year fixed mortgage
#

def mortgage(money, interestRate):
  interestRate /= 12.0
  return money*(interestRate*(1 + interestRate)**360)/((1 + interestRate)**360 - 1)

print("7.", mortgage(100000, 0.04))

# Write a Python function that determines the value of an investment after it grows due to
# compound interest.  What arguments do you need?  Where can you find the formula to use?
#
# Arguments:
#    months : months past
#    interestRate : 
#    value : value of investment

def investment(months, interestRate, value):
  for x in range(0, months):
    value += value*interestRate
  return value
  
print("8.", investment(2, 1, 1))

############################ 2d Practice Problems ############################

# Write a function that takes the temperature of H2O and returns a string describing 
# its current state ("liquid", "ice", or "steam")
#
# Arguments:
#    temp : temperature in Farenheight

def statesOfWater(temp):
  if temp < 32:
    return "Solid"
  elif temp > 212:
    return "Gas"
  else:
    return "Liquid"
  
print("9.", statesOfWater(50))

# Write a function that takes the name of a month as an argument and returns the number
# of days in that month.
#
# Note: This is according to the 2018 calendar, not a leap year.

def monthDays(monthName):
  if monthName == "January" or monthName == "March" or monthName == "May" or monthName == "July" or monthName == "August" or monthName == "October" or monthName == "December":
    return 31
  elif monthName == "Feburary":
    return 28
  else:
    return 30

print("10.", monthDays("June"))

# Write a function that is given the month, day, and year of each of two dates (six 
# arguments in all!), and determines which date comes earlier.  Return the string 
# "before" if the first date comes before the second one, "after" if the first date 
# comes after the second one, and "same" if they are the same. 

def earlierDate(day1, month1, year1, day2, month2, year2):
  if year1 < year2:
    return "before"
  elif year1 > year2:
    return "after"
  else:
      if month1 < month2:
        return "before"
      elif month1 > month2:
        return "after"
      else:
          if day1 < day2:
            return "before"
          elif day1 > day2:
            return "after"
          else:
            return "same"

print("11.", earlierDate(23, 1, 2018, 23, 1, 2018))

# Use the random package and roll two dice. Return "win" if the sum of those two
# dice is 6, 7 or 8. Return "lose" otherwise. 

def winOrLose():
  roll1 = random.randint(1, 6)
  roll2 = random.randint(1, 6)
  if roll1 + roll2 < 6:
    return "lose"
  elif roll1 + roll2 > 8:
    return "lose"
  else:
    return "win"

print("12.", winOrLose())

# Write a function that determines the number of 52-passenger school buses needed
# to transport a given number of students.

def busAmount(students):
  if students%52 == 0:
    return students/52
  else:
    return (students - students%52)/52 + 1

print("13.", busAmount(53))

# You are an olympic athlete who has just finished a race against three opponents.
# Write a function that takes all four race times as arguments (your time as the first 
# argument), and returns a string describing the medal you just won ("gold", "silver", 
# "bronze", or "no medal").  No ties!!
#
# Arguments:
#    time1 : your time
#    time2 : opponent 1's time
#    time3 : opponent 2's time
#    time4 : opponent 3's time
# Return Value:
#    what medal you recieve

def olympicMedals(time1, time2, time3, time4):
  counter = 0
  if time1 < time2:
    counter += 1
  if time1 < time3:
    counter += 1
  if time1 < time4:
    counter += 1
    
  if counter == 3:
    return "Gold!"
  elif counter == 2:
    return "Silver"
  elif counter == 1:
    return "Bronze"
  else: 
    return "No Medal"

print("14.", olympicMedals(1, 2, 3, 4))

# Write a function that takes a year and returns the boolean True if it is a leap year,
# and false if it is not.  You may need to do some research to determine the rules for leap days.
#
# Formula from https://en.wikipedia.org/wiki/Leap_year

def leapYear(year):
  if year%4 != 0:
    return False
  elif year%100 != 0:
    return True
  elif year%400 != 0:
    return False
  else:
    return True

print ("15.", leapYear(400))









