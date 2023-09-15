
infile = open("numbers.txt", "r")

numString = "" 
numList = [] 

for num in range(100): 
    numString = infile.readline()  
    while (numString != ""):  
        numList.append(int(numString)) 
        break 
infile.close()

print(numList)

def printAndSort(): 
    for num in numList: 
        print(num)
    
    for num in numList: 
        numList.sort() 
        print(num)

printAndSort() 


outfile = open("numbers.txt", "w") 
for x in range(len(numList)):
    outfile.write(str(numList[x]) + '\n') 
outfile.close()
