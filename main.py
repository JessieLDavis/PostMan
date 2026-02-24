#main menu
from gameMenu import game_menu
from optionsMenu import options_menu
from terminal_response import get_menu_response, get_multiple_choice, prompt_response
from playerChoices import search,deliver,leave
# from nav_page import selectio

def mainMenu():
    # print('GalacticPost\n')
    options = ["Play","Options"]
    userChoice = get_menu_response('',options,'GalacticPost','Intragalactic Postal Delivery',addOther=True)
    if userChoice == 'Play':
        try:
            playerObj, planetList = game_menu()
            active = True
        except Exception as e:
            active = False
        while active:
            active = playing(playerObj,planetList)
    elif userChoice == 'Options':
        options = options_menu()
    elif userChoice == 'Quit':
        return
    else:
        return mainMenu()
    return mainMenu()
    
def playing(playerObj,planetList)->bool:
    if playerObj.loc == None:
        playerObj.loc = planetList[0]
    print(playerObj.loc.welcomeMsg())
    print(playerObj.cargo())
    response = prompt_response()
    if response == 'quit':
        return False
    elif response == 'search':
        search(playerObj,planetList)
    elif response == 'deliver':
        deliver(playerObj,planetList)
    elif response == 'leave':
        leave(playerObj,planetList)
    return True

    

if '__main__' == __name__:
    mainMenu()