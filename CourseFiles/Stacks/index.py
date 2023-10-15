
def isBalanced(s):
  myStack = []

  for item in s:
    if item == "(":
      myStack.append(item)
    else: 
      myStack.pop()
  if len(myStack) > 0:
    return False
  else:
    return True
    
print(isBalanced("((((())"))
print(isBalanced("((((()))))"))
print(isBalanced("((((()))()()))"))
print(isBalanced("((((()))()()(())))"))
print(isBalanced("()()(()((()"))