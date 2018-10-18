import csv
import matplotlib.pyplot as plt
import os
import filecmp
from dateutil.relativedelta import *
from datetime import date

def getData(file):
	data= open(file, 'r')
	list_of_dict= []
	for line in data.readlines()[1:]:
		dict= {}
		values= line.split(",")
		first= values[0].strip()
		last= values[1].strip()
		email= values[2].strip()
		Class= values[3].strip()
		DOB= values[4].strip()

		dict["First"]= first
		dict["Last"]= last 
		dict["Email"]= email
		dict["Class"]= Class
		dict["DOB"]= DOB

		list_of_dict.append(dict)

	return list_of_dict


def mySort(data, key):
	sorted_list= sorted(data, key= lambda x: x[key])
	new_list= []
	for x in sorted_list:
		new_list.append((x["First"] + " " + x["Last"]))
	return new_list[0]


def classSizes(data):
	senior= 0
	junior= 0
	sophomore= 0
	freshman= 0
	for x in data:
		if x["Class"]== 'Senior':
			senior+= 1
		elif x["Class"]== 'Junior':
			junior+= 1
		elif x["Class"]== 'Sophomore':
			sophomore+= 1
		elif x["Class"]== 'Freshman':
			freshman+= 1
	classes= ['Senior', 'Junior', 'Sophomore', 'Freshman']
	number= [senior, junior, sophomore, freshman]
	class_list= (('Senior', senior), ('Junior', junior), ('Sophomore', sophomore),('Freshman', freshman))
	new_list= sorted(class_list, key= lambda x: x[-1], reverse= True)
	plt.bar(classes, number, label= 'Class Distribution', color= 'r')
	plt.show()
	return new_list


def findMonth(data):
	January= 0
	February= 0
	March= 0
	April= 0
	May= 0
	June= 0
	July=0
	August= 0
	September= 0
	October= 0
	November= 0
	December= 0
	for student in data:
		if student["DOB"].split("/")[0]== '1':
			January+= 1
		if student["DOB"].split("/")[0]== '2':
			February+= 1
		if student["DOB"].split("/")[0]== '3':
			March+= 1
		if student["DOB"].split("/")[0]== '4':
			April+= 1
		if student["DOB"].split("/")[0]== '5':
			May+= 1
		if student["DOB"].split("/")[0]== '6':
			June+= 1
		if student["DOB"].split("/")[0]== '7':
			July+= 1
		if student["DOB"].split("/")[0]== '8':
			August+= 1
		if student["DOB"].split("/")[0]== '9':
			September+= 1
		if student["DOB"].split("/")[0]== '10':
			October+= 1
		if student["DOB"].split("/")[0]== '11':
			November+= 1
		if student["DOB"].split("/")[0]== '12':
			December+= 1
	months= (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
	distribution= (January, February, March, April, May, June, July, August, September, October, November, December)
	month_distribution= list(zip(months, distribution))
	common= sorted(month_distribution, key= lambda x: x[-1], reverse= True)
	print(common)
	return common[0][0]

def mySortPrint(data, key, fileName):
	sorted_list= sorted(data, key= lambda x: x[key])
	new_list= []
	for x in sorted_list:
		new_list.append((x["First"].strip()+","+x["Last"].strip()+","+x["Email"].strip()+"\n"))
		
		final_file= open(fileName, 'w')
		for x in new_list:
			final_file.write(x)

def findAge(a):
# def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.

	pass


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
