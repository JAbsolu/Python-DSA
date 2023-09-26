# Sets are not ordered
#A set does not take in duplicate values, a value can only appear once'

myset = set()


myList = [1,2,3,4,5,6,7,8]

for num in myList:
  myset.add(num)

print(myset)

newset = set('123')
print(newset)

newestSet = set('aaabc')
print(newestSet)

#copy numbers over 3 in myset into this new set
myset2 = {item for item in myset if item > 3} 
print(myset2)