def main():
    numbers = [23, 56, 13, 78, 56, 24, 89, 19, 5]
    guess = int(input("Guess a number between 1 and 100: "))

    if guess in numbers:
        print("Good job!", guess, "is in the list.")
    else:
        print(guess, "is not in the list,", guess, "Will be added to the end of the list.")
        numbers.append(guess)
        print(numbers)

main()