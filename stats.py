def summary(games):
    if len(games) >= 1:
        for count, game in enumerate(games, 1):
            print("Game " + str(count) + " - the range of numbers was 1 to " + str(game.startinghighnum) +
                  " and the correct number was " + str(game.correctnum))

            closestnumdif = min(game.correctnum - game.lownum, game.highnum - game.correctnum)

            match game.gametype:
                case 1:
                    if game.won:
                        print(" I guessed: " + str(game.guesscount) + " times - and I won")
                    else:
                        print(" I guessed: " + str(game.guesscount) + " times - and I lost " +
                              "- I was off by " + str(abs(game.correctnum - game.currentguess)))
                case 2:
                    if game.gamewon:
                        print(" You guessed: " + str(game.guesscount) + " times - and you won")
                    else:
                        print(" You guessed: " + str(game.guesscount) + " times - and you lost " +
                              "- You were off by " + str(closestnumdif))
        print("")
    else:
        print("\nNo games found\n")

def winloss(games):
    if len(games) > 0:
        win = 0
        for game in games:
            if game.won:
                win += 1
        avg = (round(win / len(games), 3)) * 100
        print("wins: " + str(win))
        print("losses: " + str(len(games) - win))
        print("winrate: " + str(avg) + "%\n")
    else:
        print("no games found\n")

def avglength(games):
    if len(games) > 0:
        length = 0
        for game in games:
            length += game.guesscount
        length = round(length / len(games), 1)
        print("the average length of all games was " + str(length) + " rounds\n")
    else:
        print("no games found\n")

def guessesleft(games):
    if len(games) > 0:
        guesses = 0
        for game in games:
            if game.won:
                guesses += (game.maxguesses - game.guesscount)
        guesses = round(guesses / len(games), 1)
        print("the average number of guesses left was " + str(guesses) + "\n")
    else:
        print("no games found\n")
