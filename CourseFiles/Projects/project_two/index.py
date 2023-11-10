import random

capitals_dictionary = {} #Create a dictionary and saved it as capitals_dictionary

capitalsFile = open("capitals.txt", "r")  #opening the text file and saving it

for item in capitalsFile: #loop thrrought the file 
   item = item.strip() #remove space from begining & end of item
   item = item.split(',') #convert the city and state where its separated by conmma into a list

   capitals_dictionary[item[1].strip()] = item[0] #set the state to be the key & capital to be the value

capitalsFile.close() #close the text file

# PHASE 1
def findCapital():
    
    while len(capitals_dictionary) > 0: #Purposefully creating an infinite loop sunce the len will never be 0
        state = str(input("Enter a state: ")).title() #Get an input from the user, parse it to str and save it as state

        if (state in capitals_dictionary): #check if the input is in the dictionary
            print(f"The capital of the state of {state} is {capitals_dictionary[state]}") #print a quick a quick messAGE
            nextPhase = str(input("Do you want to move to phase 2? answer Y or N: ")).capitalize() #Ask the user if they would like to move to the next phase or not

            if (nextPhase == "Y"): #If they do then break the loop mve to next block of codes
                break
        else: 
            print("The entered state is not found") #Letting the user knows the entered value is invalid, start loop again
        
    totalWrongGuesses = 0 #Keeping track of wrong answers, starting at 0
    totalCorrectGuesses = 0 #keeping track of right answers, starting at 0
    totalAnswers = 0 #Keeping track of total answers

    while totalAnswers < 2: #while the number of entered answers is less than 5
        keys = list(capitals_dictionary.keys()) #Get all the keys in the dictionary
        randomNum = random.randint(0, 49) #generate random number from 0 to 49 as the keys in the list are indexed from 0 to 49
        
        guessCapital = str(input(f"What is the capital of {keys[randomNum]}: ")).capitalize().strip() #The input from the user (an input str saved as guessCapital)

        if guessCapital not in capitals_dictionary.values(): #If the entered value is not a value in the dictionary
            totalWrongGuesses += 1 #Add one to total wrong guesses
            totalAnswers += 1 #update total answers as well by adding 1
        else:
            totalCorrectGuesses += 1 #If user guessed correctly, update total correct guesses by adding 1 point
            totalAnswers += 1 #also add 1 point to total answers

    # A string to print out the final result to the user so they know how they did in the quiz
    result = f"Your total wrong answers: {totalWrongGuesses}, your total correct answers {totalCorrectGuesses}. You guessed {(int(totalCorrectGuesses) / 5 * 100)}% correct answers"

    print("Here is your result" , result) # Pring the final result

findCapital() # Invoke the function
