def askforinput(options):
    while True:
        print("Type the name or number to select an option:")
        for option in options:
            print(option[0] + ": " + option[1])

        command = str(input("")).lower()

        for option in options:
            if command in option:
                return int(option[0])
        print("\nInvalid option")


# build menus for parts of the game that ask for input
# for each tuple first item is index, second is long form description/name, third is shorthand
main = (('1', "new game", "new"),
        ('2', "show stats", "stats"),
        ('3', "exit game", "exit"))

answer = (('1', "high"),
          ('2', "low"),
          ('3', "correct"),
          ('4', "exit game", "exit"))

gametype = (('1', "you guess", "you"),
            ('2', "i guess", "me"))

statspage = (('1', "type 1"),
             ('2', "type 2"),
             ('3', "clear data", "clear"),
             ('4', "main menu", "main"))

statspagesub = (('1', "full summary", "full", "summary"),
                ('2', "win rate", "wr"),
                ('3', "avg game length", "agl"),
                ('4', "avg guesses left"),
                ('5', "go back", "back"))
