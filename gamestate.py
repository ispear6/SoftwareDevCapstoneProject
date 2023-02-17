import random
import menu
import math


class GameState:
    def __init__(self, highnum, gametype):
        self.gametype = gametype
        self.highnum = highnum
        self.maxguesses = 3 + int(math.log(highnum, 5))
        self.startinghighnum = self.highnum
    guesscount = 0
    lownum = 1
    currentguess = -1
    correctnum = 0
    won = False

    def playgame(self):
        # game type 1 has the player choose a number and the program guesses
        match self.gametype:
            case 1:
                numdif = self.highnum - self.lownum

                print("\nI have " + str(self.maxguesses) + " guesses to get it right")

                while True:
                    self.guesscount += 1
                    self.currentguess = self.lownum + (numdif // 2) + (random.randint(-(numdif // 10), numdif // 10))

                    print("\nMy guess is: " + str(self.currentguess) + " am I too high or too low?")
                    userinput = menu.askforinput(menu.answer)

                    match userinput:
                        # user exits game
                        case 4:
                            # delete unfinished games
                            del type1[-1]
                            break
                        # user says high
                        case 1:
                            self.highnum = self.currentguess - 1
                        # user says low
                        case 2:
                            self.lownum = self.currentguess + 1
                        # user says correct
                        case 3:
                            if self.guesscount > 1:
                                print("it took me " + str(self.guesscount) + " tries to get it right\n")
                            else:
                                print("it took me 1 try to get it right\n")
                            self.won = True
                            self.correctnum = self.currentguess
                            break

                    numdif = self.highnum - self.lownum

                    # checks if all possible numbers have been either guessed or ruled out and ends the game if so
                    if numdif < 0:
                        print("\nSomething went wrong, or maybe you cheated. Either way i'm ending the game.\n")
                        del type1[-1]
                        break

                    # player's win condition
                    if self.guesscount >= self.maxguesses:
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
                    self.guesscount += 1
                    # tell player how many guesses they have left
                    if 1 + (self.maxguesses - self.guesscount) > 1:
                        print("\nYou have " + str(1 + (self.maxguesses - self.guesscount)) + " guesses left")
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
                        del type2[-1]
                        break
                    # player wins
                    elif self.currentguess == self.correctnum:
                        print("\nYou win! My number was " + str(self.correctnum))
                        print("It took you " + str(self.guesscount) + " guesses to get it right")
                        self.won = True
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
                    if self.guesscount >= self.maxguesses:
                        print("\nMy number was " + str(self.correctnum))
                        print("You lose :(\n")
                        break


# create list that will contain game states for stats display
type1 = []
type2 = []
