#######################################################################
#
# Program Name: Weekday Project
# Author: Audrey Acken
# Date: 1/9/2018
#
#######################################################################

def monthName(month):
  if month == "January":
    return 1
  elif month == "February":
    return 2
  elif month == "March":
    return 3
  elif month == "April":
    return 4
  elif month == "May":
    return 5
  elif month == "June":
    return 6
  elif month == "July":  
    return 7
  elif month == "August":
    return 8
  elif month == "September":
    return 9
  elif month == "October":
    return 10
  elif month == "November":
    return 11
  elif month == "December":
    return 12
  else:
    return "error"
    
def leapYear(year):
  if year%4 != 0:
    return False
  elif year%100 != 0:
    return True
  elif year%400 != 0:
    return False
  else:
    return True

def monthDays(month, year):
  if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    return 31
  elif month == 2:
    if leapYear(year) == True:
      return 29
    else:
      return 28
  else:
    return 30
    
def weekday(month, day, year):
  yearDifference = year - 1901
  daysDifference = yearDifference*365
  for x in range(1900, year):
    if leapYear(x) == True:
      daysDifference += 1
  monthCount = monthName(month)
  for i in range(1, monthCount):
    daysDifference += monthDays(i, year)
  daysDifference += day
  dayOfWeek = daysDifference%7
  
  if dayOfWeek == 0:
    return "Monday"
  elif dayOfWeek == 1:
    return "Tuesday"
  elif dayOfWeek == 2:
    return "Wednesday"
  elif dayOfWeek == 3:
    return "Thursday"
  elif dayOfWeek == 4:
    return "Friday"
  elif dayOfWeek == 5:
    return "Saturday"
  elif dayOfWeek == 6: 
    return "Sunday"
  else:
    return "error"
    
userMonth = input("Month:")
userDay = input("Day:")
userYear = input("Year:")

userDay = int(userDay)
userYear = int(userYear)
  
print(weekday(userMonth, userDay, userYear))


  
    
  
