import random
import menu
import stats
import gamestate
from gamestate import GameState

while True:
    # display main menu
    print("\nWelcome to the game; this is a main menu of sorts.")
    userinput = menu.askforinput(menu.main)

    match userinput:
        # game mode selection
        case 1:
            print("\nWould you like me to guess the number you pick, or vise versa?")
            userinput = int(menu.askforinput(menu.gametype))

            match userinput:
                # game type 1 gameplay loop
                case 1:
                    highnum = 0

                    while 1000 > highnum < 20:
                        try:
                            highnum = int(input("Pick a number that is between 20 and 1000 to be the highest possible number: "))
                        except ValueError:
                            print("Incorrect format, integers only")

                    gamestate.type1.append(GameState(int(highnum), 1))
                    gamestate.type1[-1].playgame()
                # game type 2 gameplay loop
                case 2:
                    gamestate.type2.append(GameState(random.randint(20, 1000), 2))
                    gamestate.type2[-1].playgame()

        # show stats page
        case 2:
            while True:
                print("Which game type would you like to see?")
                userinput = menu.askforinput(menu.statspage)
                match userinput:
                    case 1:
                        userinput = menu.askforinput(menu.statspagesub)
                        match userinput:
                            case 1:
                                stats.summary(gamestate.type1)
                            case 2:
                                stats.winloss(gamestate.type1)
                            case 3:
                                stats.avglength(gamestate.type1)
                            case 4:
                                stats.guessesleft(gamestate.type1)
                    case 2:
                        userinput = menu.askforinput(menu.statspagesub)
                        match userinput:
                            case 1:
                                stats.summary(gamestate.type2)
                            case 2:
                                stats.winloss(gamestate.type2)
                            case 3:
                                stats.avglength(gamestate.type2)
                            case 4:
                                stats.guessesleft(gamestate.type2)
                    case 3:
                        gamestate.type1.clear()
                        gamestate.type2.clear()
                        print("\ndata cleared\n")
                    case 4:
                        break
        # quit the game
        case 3:
            break
