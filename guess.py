import random

wordlist = []
with open("four_letters.txt", "r") as letterfile:
    for line in letterfile:
        for word in line.split():
            wordlist.append(word)

randomword = ""
CurrentGuess = ""


def menu():
    global randomword, CurrentGuess
    print("** The Great Guessing Game **")
    randomword = random.choice(wordlist)
    CurrentGuess = "----"

menu()

def main():
    print("Current Word: " + randomword)
    print("Current guess: " + CurrentGuess)
    print("g=guess, t=tell me, l for letter, and q to quit")


main()

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
                            menu()
                            break
                main()


            else:
                print("Incorrect Guess")
                main()
        elif choice == "g":
            word = input("Enter a word:")
            if word == randomword:
                print("Guinness! you find the right word")
                menu()
                main()
            else:
                print("Oops! you failed")
                main()
        elif choice == "q":
            quitInput = input("Are you sure? (y/n)")
            if quitInput == "y":
                exit()
            else:
                done = True







