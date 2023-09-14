# This program saves a list of strings to a file.
import random


def main():
  # Create a list of strings.
  cities = ['New York', 'Boston', 'Atlanta', 'Dallas']

  # Open a file for writing.
  file = open('cities.txt', 'w')

  # Write the list to the file.
  for item in cities:
    file.write(item + '\n')

  # Close the file.
  file.close()


# Call the main function.
main()

numbers = []


def addNums():
  while len(numbers) < 100:
    numbers.append(random.randrange(1, 500))
  print(numbers)


addNums()


def writeNums():
  file = open('cities.txt', 'a')
  file.write("Adding numbers")
  numbers.sort()

  for num in numbers:
    file.write(str(num) + '\n')

  file.close()


writeNums()
