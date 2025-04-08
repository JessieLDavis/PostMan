#main menu
from gameMenu import game_menu
from optionsMenu import options_menu
# from nav_page import selectio

def mainMenu():
    options = ["Play","Options","Quit"]
    userChoice = input("Player Choice")
    if userChoice == options[0]:
        playerObj, planetList = game_menu()
        playing(playerObj,planetList)
    elif userChoice == options[1]:
        options = options_menu()
    elif userChoice == options[2]:
        return
    else:
        return mainMenu()
    
def playing(playerObj,planetList):
    if playerObj.loc == None:
        playerObj.loc = planetList[0]
    print(playerObj.loc.welcomeMsg())
    print(playerObj.cargo())
    
