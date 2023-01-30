import random
import menu
import math


class GameState:
    def __init__(self, highnum, gametype):
        self.gametype = gametype
        self.highnum = highnum
        self.maxguesses = 3 + int(math.log(highnum, 5))
        self.startinghighnum = self.highnum
    guessnum = 0
    lownum = 1
    currentguess = -1
    correctnum = 0
    gamewon = False

    def playgame(self):
        # game type 1 has the player choose a number and the program guesses
        match self.gametype:
            case 1:
                numdif = self.highnum - self.lownum

                print("\nI have " + str(self.maxguesses) + " guesses to get it right")

                while True:
                    self.guessnum += 1
                    self.currentguess = self.lownum + (numdif // 2) + (random.randint(-(numdif // 10), numdif // 10))

                    print("\nMy guess is: " + str(self.currentguess) + " am I too high or too low?")
                    userinput = menu.answermenu.askforinput()

                    # user exits game
                    if userinput in menu.answermenu.options[3]:
                        # delete unfinished games
                        del gamestatestype1[-1]
                        break
                    # user says high
                    elif userinput in menu.answermenu.options[0]:
                        self.highnum = self.currentguess - 1
                    # user says low
                    elif userinput in menu.answermenu.options[1]:
                        self.lownum = self.currentguess + 1
                    # user says correct
                    elif userinput in menu.answermenu.options[2]:
                        if self.guessnum > 1:
                            print("it took me " + str(self.guessnum) + " tries to get it right\n")
                        else:
                            print("it took me 1 try to get it right\n")
                        self.gamewon = True
                        self.correctnum = self.currentguess
                        break

                    numdif = self.highnum - self.lownum

                    # checks if all possible numbers have been either guessed or ruled out and ends the game if so
                    if numdif < 0:
                        print("\nSomething went wrong, or maybe you cheated. Either way i'm ending the game.\n")
                        del gamestatestype1[-1]
                        break

                    # player's win condition
                    if self.guessnum >= self.maxguesses:
                        print("\nI lose :(")
                        while True:
                            try:
                                self.correctnum = int(input("What was your number?\n"))
                            except ValueError:
                                print("\nIncorrect format, integers only")
                                continue
                            if self.highnum >= self.correctnum >= self.lownum:
                                break
                            else:
                                print("That can't be right, that number was ruled out or guessed already")
                        break
            # game type 2 has the program choose a number and the player guesses
            case 2:
                self.correctnum = random.randint(self.lownum, self.highnum)

                while True:
                    self.guessnum += 1
                    # tell player how many guesses they have left
                    if 1 + (self.maxguesses - self.guessnum) > 1:
                        print("\nYou have " + str(1 + (self.maxguesses - self.guessnum)) + " guesses left")
                    else:
                        print("You have 1 guess left")

                    while True:
                        # have the player input a guess or leave the game
                        try:
                            print(
                                "Pick a number between(inclusive) " + str(self.lownum) + " and " + str(self.highnum))
                            print("or input -1 to quit")
                            self.currentguess = int(input())
                        except ValueError:
                            print("\nIncorrect format, integers only")
                            continue

                        # make sure number is a possible answer
                        if self.lownum <= self.currentguess <= self.highnum or self.currentguess == -1:
                            break
                        else:
                            print("\nYou picked a number that cant be right, ill let you try again")

                    # end the game
                    if self.currentguess == -1:
                        del gamestatestype2[-1]
                        break
                    # player wins
                    elif self.currentguess == self.correctnum:
                        print("\nYou win! My number was " + str(self.correctnum))
                        print("It took you " + str(self.guessnum) + " guesses to get it right")
                        self.gamewon = True
                        break
                    # update game state to show the lowest possible number
                    elif self.correctnum > self.currentguess:
                        self.lownum = self.currentguess + 1
                        print("\nMy number is higher")
                    # update game state to show the highest possible number
                    elif self.correctnum < self.currentguess:
                        self.highnum = self.currentguess - 1
                        print("\nMy number is lower")

                    # player's loss condition
                    if self.guessnum >= self.maxguesses:
                        print("\nMy number was " + str(self.correctnum))
                        print("You lose :(\n")
                        break


# create list that will contain game states for stats display
gamestatestype1 = []
gamestatestype2 = []
