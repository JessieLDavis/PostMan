#main menu
from gameMenu import game_menu
from optionsMenu import options_menu
from terminal_response import get_menu_response, get_multiple_choice, prompt_response, PLAYER_OPTS
from playerChoices import search,deliver,leave,show_map,get_player_status, refuel,influence
from nav_page import Planet
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
            print(e)
            active = False
        while active:
            active = playing(playerObj,planetList)
    elif userChoice == 'Options':
        options = options_menu()
    elif userChoice == 'Quit':
        return
    else:
        return mainMenu()
    # return mainMenu()
    
def playing(playerObj,planetObj:Planet)->bool:
    if playerObj.loc == None:
        playerObj.loc = planetObj.post_office
    print(playerObj.loc.welcomeMsg())
    print(playerObj.cargo())
    response = prompt_response()
    if response == 'quit':
        return False
    elif response == 'search':
        search(playerObj,planetObj)
    elif response == 'deliver':
        deliver(playerObj)
    elif response == 'leave':
        leave(playerObj,planetObj)
    elif response == 'map':
        show_map(planetObj,planetObj)
    elif response == 'status':
        get_player_status(playerObj)
    elif response == 'influence':
        influence(playerObj)
    elif response == 'check fuel':
        percF = playerObj.check_fuel(False)
        print(f"Fuel at {percF*100}%")
    elif response == 'refuel':
        refuel(playerObj)
    return True

    

if '__main__' == __name__:
    mainMenu()