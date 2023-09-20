'''
code walkthrough
My steps for the project
1. save an empty list as populationList
2. define a function and name it getData()
3. open the file population.txt file and pass the r argument to read the file,
save it as populationFile
4. loop through the file and append each line to the population list
5. close the file
6. invoke the getData() function

Phase 2:
1. define a new function and name it putData(), pass it a paramater
2. loop the list passed in the function, print each item in the list
3. Invoke the putData function and pass the population list as its argument 

phase3:
1. create a list and save it as populationDifference
2. defined a function and name it anualIncrease and pass it a parameter
and name it aList
3. declare variable i and set it to 0, and j set it to equal
the value of i plus 1 (this will make sure, j always point to the i's next index)
4. subtract the value at index j by the index of i to get the difference,
then add the diffrence to the populationDifference list.
5. when the loop ends, sort the list from smallest to biggest
6. 
'''

# Phase1
populationList = []

def getData():
  populationFile = open("population.txt", "r")
  for population in populationFile:
    populationList.append(int(population))
  populationFile.close()


getData()  #Call the function


# Phase 2
def putData(a_list):
  for num in a_list:
    print(num)


# Phase 3
populationDifference = []  #the empty list

def anualIncrease(aList):
  i = 0
  j = i + 1
  year = 1950
  while i < len(aList) - 1 and j < len(aList) - 1:
    #append population increase & year
    populationDifference.append(
        f"{int(aList[j]) - int(aList[i])} in year {year}")
    i += 1  #increment i
    j += 1  #increment j
    year += 1  #add 1 to the year
  populationDifference.sort()

#invoke the anual increase function
anualIncrease(populationList)  

#call the putData function created in phase2
putData(populationDifference)  

#save lowest population increase
lowestIncrease = min(populationDifference)  

#save highest population increase
highestIncrease = max(populationDifference)  

# prints the lowest population increase
print(f'The lowest population increase was {lowestIncrease}')
# prints the highest population increase
print(f'The highest population increase was {highestIncrease}')
