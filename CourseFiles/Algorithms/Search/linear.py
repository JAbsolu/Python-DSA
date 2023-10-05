#Linear search runs at O(n)

MyList = [1,2,3,4,5,6,7,8]

def findNum(n):
  for num in MyList:
    if n == num:
      return f"Found: {n}"
      
  print(f"{n} was not found")

print(findNum(5))
print(findNum(10))