import random

myList = [[1,2,3,4], [9,8,7,6], [5,8,2,4]]

for i in range(len(myList)):
  value = myList[i]
  print(value)
  for j in range(len(value)):
    print(value[j])

print(f'Orginal list: {myList}')

for i in range(len(myList)):
  value = myList[i]
  print(value)
  for j in range(len(value)):
    myList[i][j] = random.randint(1,100)

print(f'New list: {myList}')