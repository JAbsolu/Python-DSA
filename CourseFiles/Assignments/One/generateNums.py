import random

numbers = []

def generateNums():
    while len(numbers) < 100:
        numbers.append(random.randrange(1, 500, 100))
    print(numbers)

generateNums()

def printnum():
    numbers.sort()
    for x in numbers:
        print("%10d" %x, end="wow cool")
printnum()



def printNums():
    for num in numbers:
        print(num)
printNums()


def printNumst():
    list = ''
    for num in numbers:
        list +=" " + str(num)
        # print(num)
    print(list)
printNumst()


def sortAndReverse():
    numbers.sort()
    numbers.reverse()
    print(numbers)
sortAndReverse()


def findANum():
    num = int(input("Enter a number between 1 to 500: "))

    if num in numbers:
        counteNum = numbers.count(num)
        print(f'{num} appeared in the numbers list {counteNum} times.')
    else:
        print(f'{num} is not in the numbers list.')
findANum()


print(max(numbers))