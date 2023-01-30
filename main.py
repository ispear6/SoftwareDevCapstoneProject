import random
import menu
import stats
import gamestate
from gamestate import GameState

while True:
    # display main menu
    print("\nWelcome to the game; this is a main menu of sorts.")
    userinput = menu.mainmenu.askforinput()

    # quit the game
    if userinput in menu.mainmenu.options[2]:
        break

    # game mode selection
    elif userinput in menu.mainmenu.options[0]:
        print("\nWould you like me to guess the number you pick, or vise versa?")
        userinput = menu.gametypemenu.askforinput()

        # game type 1 gameplay loop
        if userinput in menu.gametypemenu.options[0]:
            highnum = 0

            while 1000 > highnum < 20:
                try:
                    highnum = int(input("Pick a number that is between 20 and 1000 to be the highest possible number: "))
                except ValueError:
                    print("Incorrect format, integers only")

            gamestate.gamestatestype1.append(GameState(int(highnum), 1))
            gamestate.gamestatestype1[-1].playgame()
        # game type 2 gameplay loop
        elif userinput in menu.gametypemenu.options[1]:
            gamestate.gamestatestype2.append(GameState(random.randint(20, 1000), 2))
            gamestate.gamestatestype2[-1].playgame()

    # show stats page
    elif userinput in menu.mainmenu.options[1]:
        while True:
            print("Which game type would you like to see?")
            userinput = menu.statspagemenu.askforinput()
            if userinput in menu.statspagemenu.options[0]:
                stats.showstats(gamestate.gamestatestype1)
            elif userinput in menu.statspagemenu.options[1]:
                stats.showstats(gamestate.gamestatestype2)
            elif userinput in menu.statspagemenu.options[2]:
                gamestate.gamestatestype1.clear()
                gamestate.gamestatestype2.clear()
                print("\ndata cleared\n")
            elif userinput in menu.statspagemenu.options[3]:
                break
