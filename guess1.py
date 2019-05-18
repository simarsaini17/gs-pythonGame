import random
from stringDatabase import stringDatabase

class guess1:

    randomword = ""
    CurrentGuess = ""
    NumberofAttempts=""
    BadGuess = 0
    Gamecounter = 0
    MissedLetters = 0
    initialscore=0
    # finalscore=0

    def menu(self):
        global randomword, CurrentGuess
        print("** The Great Guessing Game **")
        c2 = stringDatabase()
        randomword = random.choice(c2.read_file())
        CurrentGuess = "----"

    def user_choice(self):
        global randomword, CureentGuess
        print("Current Word: " + randomword)
        print("Current guess: " + CurrentGuess)
        print("g=guess, t=tell me, l for letter, and q to quit")

    def startgame(self):
        global randomword, CurrentGuess, BadGuess, Gamecounter
        global MissedLetter, initalscore
        game_lives = 100
        while game_lives >= 1:
            done = True
            while done:

                choice = input("Enter a choice:")
                print(choice)
                if choice == "l":
                    letter = input("Enter a Letter: ")
                    if letter in randomword:
                        guesscount = 1
                        print("You found %d letter " % (guesscount))
                        for i in range(0, len(randomword)):
                            if letter == randomword[i]:
                                CurrentGuess = CurrentGuess[:i] + letter + CurrentGuess[i + 1:]
                                if CurrentGuess == randomword:
                                    GuessingGame.menu()
                                    break

                        GuessingGame.user_choice()
                    else:
                        self.MissedLetters=self.MissedLetters+1
                        print("Incorrect Guess")
                        GuessingGame.user_choice()

                elif choice == "g":
                    word = input("Enter a word:")
                    if word == randomword:
                        print("Guinness! you find the right word")
                        GuessingGame.menu()
                        GuessingGame.user_choice()
                    else:
                        self.BadGuess=self.BadGuess+1
                        print("Oops! you failed")
                        GuessingGame.user_choice()

                elif choice == "t":
                    print("Big loser! " + randomword)

                elif choice == "q":
                    quitInput = input("Are you sure? (y/n)")
                    if quitInput == "y":
                        exit()
                    else:
                        done = True



GuessingGame = guess1()
GuessingGame.menu()
GuessingGame.user_choice()
GuessingGame.startgame()





