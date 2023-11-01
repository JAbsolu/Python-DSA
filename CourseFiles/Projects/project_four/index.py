''''
Author: John Absolu
CSC 212
Programming Assignment: Project 4
Program Description: Postfix Evaluation (Stacks)
''' ''
'''
The function below is the main function that will be called when the program is run.
'''


def main():
  '''
    Below is the stack class
  '''

  class Stack():
    '''
      self.items = [] -- this line initiate an empty list
      isEmpty() -- checks if the stack is empty and returns a boolean of true or false
      push() -- adds an item to the stack
      pop() -- removes an item from the stack
      peek() -- returns the top item in the stack
      size() -- returns the size of the stack
    '''

    def __init__(self):
      self.stack = []

    def isEmpty(self):
      return self.stack == []

    def push(self, item):
      self.stack.append(item)

    def pop(self):
      return self.stack.pop()

    def peek(self):
      return self.stack[len(self.items) - 1]

    def size(self):
      return len(self.stack)

  '''
    valuate_postfix(expression) -- Is the function that evaluate the postfix
    It takes a paramater named expression that will later be used to pass an 
    argument when the function is called.    
  '''

  def evaluate_postfix(expression):
    '''
      stack -- Creates a new stack
      tokens -- tokens is each item in the expression
      token -- Each item tokens
      token.isdigit() -- checks if the item is a digit,
      if it is, I add it to the stacl (on top of current items in stack)
      if it is not 
        operand2 -- saves the first seeing operand in the stack
        operand1 -- saves the next operand seing in the stack

        the inner if statement checks to make sure that both operands exist
        then i check if the token is a valid operator, if yes
        I save the sum of operand1 and operand2 in result
        Finally after the if else chain add the result to the stack.
    '''
    stack = Stack()

    tokens = expression.split()

    for token in tokens:
      if token.isdigit():
        stack.push(int(token))
      else:
        operand2 = stack.pop()
        operand1 = stack.pop()

        if operand1 is not None and operand2 is not None:
          if token == '+':
            result = operand1 + operand2
          elif token == '-':
            result = operand1 - operand2
          elif token == '*':
            result = operand1 * operand2
          elif token == '/':
            result = operand1 / operand2

          stack.push(result)

    '''
      The if and else block code below 
      1 -- checks if the size of the stack is 1
      2 -- If true, return item in the stack
      3 -- if false raise an except (error)
    '''
    if len(stack.stack) == 1:
      return stack.pop()
    else:
      raise ValueError("Invalid postfix expression")

  '''
    The block of code below, uses the try exept block to catch for errors
    1. Try -- This checks if the code runs withouth error
    2. Except -- if this line runs that means there is an error, I then 
    print the error.
  '''
  postfix_expression = "3 5 1 - * 2 +"
  try:
    result = evaluate_postfix(postfix_expression)
    print(f"The result of the postfix expression is: {result}")
  except ValueError:
    print(ValueError)


if __name__ == "__main__":
  main()
