import csv
import matplotlib.pyplot as plt
import numpy as np

name = "iron"
secondname = "ferrous sulfate"

#name = "vitamin c"
#secondname = "ascorbic acid"

#name = "thiamine mononitrate"
#secondname = "vitamin b1"

#name = "vitamin b12"
#secondname = "cyancocobalamin"

#name = "thiamin mononitrate"
#secondname = "vitamin b1"

#name = "pyridoxine hydrochloride"
#secondname = "vitamin b6"

#name = "tocopherols"
#secondname = "vitamin e"

#name = "vitamin b3"
#secondname = "niacin"

#name = "vitamin b2"
#secondname = "riboflavin"

def countformatting(name,secondname):
  name = name.lower()
  secondname = secondname.lower()

#header for the new file
header = ['id', 'ingredientlist']

#create new file called ingredientsearch.csv
with open ('ingredientsearch.csv', 'w', encoding = 'UTF8') as searchcsv:
  writerforfile = csv.writer(searchcsv)
  writerforfile.writerow(header)

  #open the original OpenFoodFactsDatabase.csv
  with open ('OpenFoodFactsDatabase.csv', newline ='') as originalcsv:
    reader = csv.DictReader(originalcsv)

    for row in reader:
      id = row['code']
      ingredientslist = row['ingredients_text']

      if row['ingredients_text'].find(name) != -1 or row['ingredients_text'].find(secondname) != -1:
         data =[id, ingredientslist]
         writerforfile.writerow(data)

  searchcsv.close()
  originalcsv.close()

  with open('ingredientsearch.csv','r', newline ='') as searchcsv:
    reader2 = csv.DictReader(searchcsv)

    #declaring count variables for future use in code
   
    nameparensecondcount = 0
    namecurlybracketsecondcount = 0
    namesquarebracketsecondcount = 0 
    
    secondparennamecount = 0
    secondcurlybracketnamecount = 0
    secondsquarebracketnamecount = 0

    seconditselfcount = 0
    nameitselfcount = 0

    for row in reader2:
     
     
     if  (name + " (" + secondname + ")") in row['ingredientlist']:
      nameparensecondcount +=1

     if (name + " {" + secondname + "}") in row['ingredientlist']:
      namecurlybracketsecondcount +=1

     if (name+" [" + secondname +"]") in row['ingredientlist']:
      namesquarebracketsecondcount +=1

     if (secondname + " (" + name + ")") in row['ingredientlist']:
      secondparennamecount +=1

     if (secondname + " {" + name + "}") in row['ingredientlist']:
      secondcurlybracketnamecount +=1

     if (secondname+" [" + name + "]") in row['ingredientlist']:
      secondsquarebracketnamecount +=1

     if name in row['ingredientlist']:
      nameitselfcount +=1

     if secondname in row['ingredientlist']:
      seconditselfcount +=1

seconditselfcount = seconditselfcount - secondsquarebracketnamecount - secondcurlybracketnamecount -secondparennamecount-namesquarebracketsecondcount-namecurlybracketsecondcount-nameparensecondcount

nameitselfcount = nameitselfcount- secondsquarebracketnamecount - secondcurlybracketnamecount -secondparennamecount-namesquarebracketsecondcount-namecurlybracketsecondcount-nameparensecondcount


print("The amount of times that " + name + " (" + secondname + ") is " + str(nameparensecondcount))

print("The amount of times that " + name + " {" + secondname + "} is " + str(namecurlybracketsecondcount))

print("The amount of times that " + name + " [" + secondname + "] is " + str(namesquarebracketsecondcount))

print("The amount of times that " + secondname + " (" + name + ") is " + str(secondparennamecount))

print("The amount of times that " + secondname + " {" + name + "} is " + str(secondcurlybracketnamecount))

print("The amount of times that " + secondname + " [" + name + "] is " + str(secondsquarebracketnamecount))

print("The amount of times that " + name + " is " + str(nameitselfcount))

print("The amount of times that " + secondname + " is " + str(seconditselfcount))


#creating bar graph

counts = [nameparensecondcount,namecurlybracketsecondcount,namesquarebracketsecondcount, secondparennamecount, secondcurlybracketnamecount, secondsquarebracketnamecount, nameitselfcount, seconditselfcount ]

labels = ['iron (ferrous sulfate)', 'iron {ferrous sulfate}', 'iron [ferrous sulfate]', 'ferrous sulfate (iron)', 'ferrous sulfate {iron}', 'ferrous sulfate [iron]', 'iron', 'ferrous sulfate']


figure = plt.figure(figsize = (8,8))
plt.xlabel("Formatting Differences")
plt.ylabel("Count")
plt.xticks(rotation=90)

#https://stackabusecom/change-tick-frequency-in-matplotlib
y = np.random.randint(low=0, high=50, size=100)
# https://www.programmersought.com/article/49946523532/
plt.yticks(np.arange(min(y), max(y)+2, 2.0))

plt.bar(labels,counts)

plt.savefig("differentformats.png",dpi=300, bbox_inches = "tight")

plt.show()