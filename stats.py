def showstats(gamestates):
    if len(gamestates) >= 1:
        for count, game in enumerate(gamestates, 1):
            print("Game " + str(count) + " - the range of numbers was 1 to " + str(game.startinghighnum) +
                  " and the correct number was " + str(game.correctnum))
            match game.gametype:
                case 1:
                    if game.gamewon:
                        print(" I guessed: " + str(game.guessnum) + " times - and I won")
                    else:
                        print(" I guessed: " + str(game.guessnum) + " times - and I lost " +
                              "- I was off by " + str(abs(game.correctnum - game.currentguess)))
                case 2:
                    if game.gamewon:
                        print(" You guessed: " + str(game.guessnum) + " times - and you won")
                    else:
                        print(" You guessed: " + str(game.guessnum) + " times - and you lost " +
                              "- You were off by " + str(abs(game.correctnum - game.currentguess)))
        print("")
    else:
        print("\nNo games found\n")
