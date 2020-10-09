'''
This program reads through all the files in the Data_files folder for specific keywords
looks for cities around the world with specific keywords in their name

Written by Michael Gromski for Tyler Grober
'''
import os

keyword = 'uwu'

dataPath = "Data_files\\"
names = []
lat = []
lng = []
sucess = [[],[],[]]
failedcount = 0
for item in os.listdir(dataPath):
    dest =  "Data_files\\" + str(item)
    file = open(dest)
    try:
        for line in file:
            line.strip("\n")
            element = line.split("\t")
            names.append(element[2])
            lat.append(element[4])
            lng.append(element[5])
    except:
        failedcount += 1
print(f"Searched {len(names)} cities, unable to read {failedcount} cities.")

#now lets look for cities with our keywords
for i in range(len(names)):
    if (names[i].find(keyword) != -1):
        sucess[0].append(names[i])
        sucess[1].append(lat[i])
        sucess[2].append(lng[i])
print(f"Able to find {len(sucess[1])} cities/towns with {keyword} in the name!")
print("They are:")
for i in range(len(sucess[0])):
    print(f"{sucess[0][i]}")