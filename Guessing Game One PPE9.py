#module-imports
import random

#global-variables
userChoice = " "
randomNum = 0
guesses = 0
correctGuess = False

#main
randomNum = random.randint(1,9)
while userChoice != "exit" and correctGuess == False:
    userChoice = input("Please enter your guess, between 1 and 9 (inclusive). To exit, type 'exit'.")
    guesses +=1
    if userChoice == "exit":
        print("Okay. goodbye!")
    else:
        try:
            userChoice = int(userChoice)
            if userChoice == randomNum:
                if guesses == 1:
                    print("Wow you got it in 1 try! Impressive.")
                else:
                    print(f"Wow you got it! Only took you {guesses} tries!")
                correctGuess = True
            elif userChoice >randomNum:
                print("Guess is too high!")
            else:
                print("Guess is too low!")
        except:
            print("That was NOT a valid input! Try again.")












