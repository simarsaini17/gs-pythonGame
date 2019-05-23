'''
@author: Gursimrat kaur
'''

import random
from stringDatabase import StringDatabase
from game import Game

class Guess:
    '''
    Guess class display the game menu

    Attributes:
        randomword(str): word randomly selected from file
        CurrentGuess(str): number of letters uncovered
        letterrequest(int): number of times user request to guess the word by letter
        myInstance[](object): array of gameobject

    Methods:
        menu(): display starting menu of the game
        user_choice(): display choice
        startgame(): take the
        game_status(): display the table of values for each game and show the total score

    '''
    randomword = ""
    CurrentGuess = ""
    letterrequest = 0
    myInstances=[]



    def menu(self):
        '''
        Display message when game starts

        :return: return nothing
        '''
        global randomword, CurrentGuess
        print("** The Great Guessing Game **")
        c2 = StringDatabase()
        randomword = random.choice(c2.read_file())
        CurrentGuess = "----"


    def user_choice(self):
        '''
        Display current guess and choice menu
        g is for word guess
        t is for display the word
        l is for letter guess
        q is to quit the game

        :return: return nothing
        '''
        global randomword, CureentGuess
        print("Current guess: " + CurrentGuess)
        print("g=guess, t=tell me, l for letter, and q to quit")

    def startgame(self):
        '''
        create game object
        ask user input choice for guessing word

        :return: return nothing

        '''

        global randomword, CurrentGuess
        game_lives = 100
        while game_lives >= 1:
            gameobject = Game(randomword)
            done = True

            while done:
                choice = input("Enter a choice:")
                print(choice)
                if choice == "l":
                    self.letterrequest = self.letterrequest + 1
                    letter = input("Enter a Letter: ")
                    gameobject.letter_guess(letter)

                    if letter in randomword:
                        guesscount = 1
                        print("You found %d letter " % (guesscount))
                        for i in range(0, len(randomword)):
                            if letter == randomword[i]:
                                CurrentGuess = CurrentGuess[:i] + letter + CurrentGuess[i + 1:]
                                if CurrentGuess == randomword:
                                    GuessingGame.menu()
                                    done= False

                        GuessingGame.user_choice()

                    else:
                        print("This is not the correct guess")
                        GuessingGame.user_choice()

                elif choice == "g":
                    word = input("Enter a word:")
                    gameobject.word_guess(word)
                    if word == randomword:
                        print("Guinness! you find the right word")
                        done= False
                        GuessingGame.menu()
                        GuessingGame.user_choice()
                    else:
                        print("Oops ! you failed")
                        GuessingGame.user_choice()

                elif choice == "t":
                    gameobject.show_word()
                    print("Big loser! " + randomword)
                    done=False
                    GuessingGame.menu()
                    GuessingGame.user_choice()

                elif choice == "q":
                    quitInput = input("Are you sure? (y/n)")
                    if quitInput == "y":
                        GuessingGame.game_status()
                        exit()
                    else:
                        done = True

                else:
                    print("Enter Correct Option")

            GuessingGame.myInstances.append(gameobject)
            game_lives=game_lives-1

    def game_status(self):
        '''
        Display table of values for each game user played and show total game score

        :return: return nothing

        '''
        sum=0
        coloum_format="{:>5}{:>10}{:>10}{:>15}{:>20}{:>10}"
        row_format="{:>5d}{:>10s}{:>10s}{:>15d}{:>20d}{:>10.2f}"
        print (coloum_format.format("Game","Word","Status","Bad Guess","Missed Letters","Score"))
        print (coloum_format.format("----","----","------","---------","--------------","-----"))

        for obj in self.myInstances:
            if obj.score > 0 and self.letterrequest>0:
                obj.score /= self.letterrequest
            print(row_format.format(self.myInstances.index(obj)+1,obj.answer,obj.status,obj.badguess,obj.missedletter,obj.score))
            sum = sum+obj.score

        print("\n Final Score : {:5.2f}".format(sum))


if __name__=="__main__":
    GuessingGame = Guess()
    GuessingGame.menu()
    GuessingGame.user_choice()
    GuessingGame.startgame()







