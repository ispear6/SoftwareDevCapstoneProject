class Menu:
    def __init__(self, options):
        self.options = options

    def askforinput(self):
        while True:
            print("Type the name or number to select an option:")
            for option in self.options:
                print(option[0] + ": " + option[1])

            command = str(input("")).lower()

            if any(command in option for option in self.options):
                return command
            else:
                print("\nInvalid option")


# build menus for parts of the game that ask for input
# for each tuple first item is index, second is long form description/name, third is shorthand
mainmenuitems = (('1', "new game", "new"),
                 ('2', "show stats", "stats"),
                 ('3', "exit game", "exit"))

answermenuitems = (('1', "high"),
                   ('2', "low"),
                   ('3', "correct"),
                   ('4', "exit game", "exit"))

gametypemenuitems = (('1', "you guess", "you"),
                     ('2', "i guess", "me"))

statspagemenuitems = (('1', "type 1"),
                      ('2', "type 2"),
                      ('3', "clear data", "clear"),
                      ('4', "main menu", "main"))

# instantiate menus
mainmenu = Menu(mainmenuitems)
answermenu = Menu(answermenuitems)
gametypemenu = Menu(gametypemenuitems)
statspagemenu = Menu(statspagemenuitems)
