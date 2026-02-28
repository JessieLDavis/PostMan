#main menu
import os
from gameMenu import game_menu, save_game
from optionsMenu import options_menu
from terminal_response import get_menu_response, get_multiple_choice, prompt_response, PLAYER_OPTS, get_binary_response
from playerChoices import search,deliver,leave,show_map,get_player_status, refuel,influence
from nav_page import Planet
# from nav_page import selectio

PLAYER_SAVE = "player/player_save.json"

def mainMenu():
    # print('GalacticPost\n')
    options = ["Play","Options"]
    userChoice = get_menu_response('',options,'GalacticPost','Intragalactic Postal Delivery',addOther=True)
    if userChoice == 'Play':
        try:
            playerObj, planetList = game_menu(PLAYER_SAVE)
            active = True
        except Exception as e:
            print(e)
            active = False
        while active:
            os.system('cls')
            active = playing(playerObj,planetList)
            
        confirm_save = get_binary_response('Would you like to save?')
        if confirm_save == True:
            save_game(PLAYER_SAVE,playerObj,planetList)
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
    print(f'-'*50)
    print()
    print(playerObj.loc.welcomeMsg())
    # print action?
    if playerObj.message != '':
        print(f"> {playerObj.message}")
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