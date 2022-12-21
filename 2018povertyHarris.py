# -*- coding: utf-8 -*-

import requests as req
import csv

tableRows = []

#Collect url codes for Harris County boys who lived in poverty in 2018
i=4
istr=str(i)
while i < 10:
    istr = str(i)
    tableRows.append("B17001_00"+istr+"E")
    i += 1

#Collect url codes Harris County girls who lived in poverty in 2018
i=18
while i < 24:
    istr = str(i)
    tableRows.append("B17001_0"+istr+"E")
    i += 1

#Pulling and adding everyone under 18 living in poverty in Harris County in 2018.
url = "census.gov"
under18poverty = 0 #if only, right?
print("working...")
for row in tableRows:
    url = "https://api.census.gov/data/2018/acs/acs1?get=NAME,"+row+"&for=county:201&in=state:48"

    response = req.get(url,)
    under18poverty += int(response.json()[1][1])
    #dictionary[response.json()[0][1]] = int(response.json()[1][1]) #We're not doing this anymore but I don't want to erase it yet.
    #Printing dots so that you know the thing hasn't crashed.
    print("...")

#Pulling stats for everyone who lived in poverty in Harris County in 2018.
url = "https://api.census.gov/data/2018/acs/acs1?get=NAME,B17001_002E&for=county:201&in=state:48"
response = req.get(url,)
totalPoverty = int(response.json()[1][1])

#Pulling stats for the median household income for Harris County in 2018.
url = "https://api.census.gov/data/2018/acs/acs1?get=NAME,B19013_001E&for=county:201&in=state:48"
response = req.get(url,)
medianIncome = int(response.json()[1][1])

#Throwing all those stats into a dictionary.
dictionary = {
    "poverty under 18" : under18poverty,
    "poverty any age" : totalPoverty,
    "median income" : medianIncome
    }

#printing for reassurance
print("(now writing to csv...)")
#writing dictionary to csv
with open('test.csv', 'w') as f:
    for key in dictionary.keys():
        f.write("%s,%d\n"%(key,dictionary[key]))