import requests
from bokeh.plotting import figure, show
import numpy as np
f = figure()
'''
# 1. Create a dictionary that has the country name as a key and the capital 
#    of that country as the value.

f = {"fields" : "name;capital"}

url = "https://restcountries.eu/rest/v2/all?"

r = requests.get(url, params = f)

data = r.json()

capitals = {}

for country in data:
  capitals[country["name"]] = country["capital"]
  
print(capitals)

# 2. Create a dictionary that has the country name as the key and the number
#    of people per square mile as the value.  (Hint: divide population by area) 

f = {"fields" : "name;population;area"}

url = "https://restcountries.eu/rest/v2/all?"

r = requests.get(url, params = f)

data = r.json()

peoplePerSquareMile = {}

for country in data:
  if "area" in country  and "population" in country:
    peoplePerSquareMile[country["name"]] = float(country["population"]) / float(country["area"])

print(peoplePerSquareMile)

# 3. Create a text file called usa-milk.txt where every row is the city and the
#    cost of milk in that city (separated by a comma).  You do not need to do 
#    the USA or even milk but you do need to pick a country with a lot of cities.

url = "https://numbeo.com/api/"

f = {"api_key" : "0jalvgng5h70u2", "country" : "United States"}
r = requests.get(url + "cities?", params = f)

data = r.json()

data = data["cities"]

cities = []
for city in data:
  cities.append((city["city"],city["city_id"]))


for (city,cityID) in cities:
  f2 = {"api_key" : "0jalvgng5h70u2", "city_id" : cityID}
  r2 = requests.get(url + "city_prices?", params = f2)
  data2 = r2.json()
  data2 = data2["prices"]
  for item in data2:
    if item["item_name"] == "Milk (regular), (1 liter), Markets":
      a = open("usa-milk.txt", "a")
      a.write(city + "," + str(item["average_price"]) + "\n")

# 4. First, create a text file called quality-of-life.txt  where every row contains
#    the name of a country and the quality of life for that country (separated by a "|").
#    Second, create a horizontal bar chart for this dataset.  The bar chart should
#    be ordered.  Meaning the country with the best quality of life at the top of 
#    the bar chart and the lowest quality of life at the bottom.

url = "https://numbeo.com/api/"

f = {"api_key" : "0jalvgng5h70u2"}

r = requests.get(url + "cities?", params = f)

dict = {}

data = r.json()
data = data["cities"]

countries = []
for city in data:
  if city["country"] not in countries:
    countries.append(city["country"])
    
for country in countries:
  f2 = {"api_key" : "0jalvgng5h70u2", "country" : country}
  r2 = requests.get(url + "country_indices?", params = f2)
  data2 = r2.json()
  if "quality_of_life_index" in data2:
    #a = open("quality-of-life.txt", "a")
    #a.write(country + "|" + str(data2["quality_of_life_index"]) + "\n")
    dict[country] = data2["quality_of_life_index"]
    
sort = [(k, dict[k]) for k in sorted(dict, key=dict.get, reverse = True)]

xVals = []
yVals = []
for i in range(0,len(sort)):
    xVals.append(sort[i][0])
    yVals.append(sort[i][1])
f = figure(x_range=xVals, title="Quality of Life", toolbar_location=None, tools="", width = 1300)
f.vbar(x=xVals, top=yVals, width=0.9)
f.xaxis.major_label_orientation = "vertical"

show(f)
'''  
# 5. Create a scatter plot where every dot is colored by region. On the x-axis 
#    place the crime index and the y-axis place the quality of life index. If you
#    would like to reduce it to a single country and compare indices per city that's
#    fine too.  Should look something like this. I used both API's so mine is colored
#    based on their continent and also sized based on the population. From this 
#    graph you can clearly see that there is a correlation between people's safety
#    and their quality of life.

url = "https://numbeo.com/api/"

f = {"api_key" : "0jalvgng5h70u2"}

r = requests.get(url + "cities?", params = f)

dict = {}

data = r.json()
data = data["cities"]

countries = []
for city in data:
  if city["country"] not in countries:
    countries.append(city["country"])
xVals = []
yVals = []
sizes = []
colors = []
for country in countries:
  f2 = {"api_key" : "0jalvgng5h70u2", "country" : country}
  r2 = requests.get(url + "country_indices?", params = f2)
  data2 = r2.json()
  if ("quality_of_life_index" in data2) and ("crime_index" in data2):
    r3 = requests.get("https://restcountries.eu/rest/v2/name/" + country + "?fullText=true")
    data3 = r3.json()
    if (len(data3) == 1):
      if ("population" in data3[0]) and ("region" in data3[0]):
        xVals.append(data2["crime_index"])
        yVals.append(data2["quality_of_life_index"])
        if (data3[0]["population"] > 1000000000):
          sizes.append(40)
        elif (data3[0]["population"] > 100000000):
          sizes.append(32)
        elif (data3[0]["population"] > 10000000):
          sizes.append(24)
        elif (data3[0]["population"] > 1000000):
          sizes.append(16)
        elif (data3[0]["population"] > 50000):
          sizes.append(8)
        else:
          sizes.append(2)
        if (data3[0]["region"] == "Asia"):
          colors.append("black")
        elif (data3[0]["region"] == "Europe"):
          colors.append("green")
        elif (data3[0]["region"] == "Africa"):
          colors.append("red")
        elif (data3[0]["region"] == "Americas"):
          colors.append("yellow")
        elif (data3[0]["region"] == "Oceania"):
          colors.append("blue")
        else:
          print(data3[0]["region"])
          colors.append("orange")

f = figure()
f.circle(xVals, yVals, size=sizes, color=colors)
show(f)
        
'''
# ***Write a short reflection on one of the following visuals.  What do you notice?
# Which country is at the top? What about the bottom? Are there any surprises?***

There is a pretty distinct linear relationship between crime rate and quality of life, which
can be expected (lower crime rate equals higher quality of life). It would be interesting to see
if there is a causal relationship between them (which one causes the other) , or if both factors 
affect each other equally.There isn't much of a correlation with population size and quality of
life/crime rate, as they are dispersed pretty evenly (although the European countries, 
which are green, tend to be on the smaller side of population). Looking at the graph through a 
regional lens, european and oceanian countries tend to be on the higher quality of life and 
lower crime rate side of the graph, african countries tend to be on the lower quality of life and
higher crime rate side, american countries crowd around the median quality of life and high crime
rate side, and asian countries are pretty well dispersed between all of them. I wasn't very suprised
by the general trends, but there was one outlier which had a low crime rate and low quality of life.

'''
    
    



