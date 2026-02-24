from random import choice, choices
from assets.animations import *
from terminal_response import get_multiple_choice, get_planet_choice

def search(playerObj,planetClass):       
    # choice_range = range(30,step=2)
    num = choice(range(0,30,2))
    if num == 0:
        print("No packages found.")
        return playerObj
    destination = [plan for plan in planetClass.planet_dict.items() if plan != playerObj.loc]
    origin = playerObj.loc
    destination = choice(destination)
    product = choice(playerObj.loc.products)
    selection = (num,destination,product,origin)
    print(f'Loaded {num} {product} to deliver to {destination.showLoc()}')
    if playerObj.loc.nameL == "Post Office":
        playerObj.cargoManifest["letters"].append(selection)
    else:
        playerObj.cargoManifest["packages"].append(selection)
    return playerObj

def deliver(playerObj,anySuccess=False):
    letterList = [plan for plan in playerObj.cargoManifest["letters"] if plan[1] == playerObj.loc]
    packageList = [plan for plan in playerObj.cargoManifest["packages"] if plan[1] == playerObj.loc]
    deliverList = letterList + packageList
    if len(deliverList) != 0:
        print('Unloading cargo.')
        for item in deliverList:
            number, destination, product, origin = item
            playerObj.loc.playerImpact += number
            # playerObj.points += (number*10)
            newPts = (number+destination.playerImpact)*10
            playerObj.points += newPts

            destination.playerImpact += number
            try:
                destination.planetRelations[origin]
            except KeyError:
                destination.planetRelations[origin] = 0
            destination.planetRelations[origin] += number

            print(f'{number} {product} delivered!')
            print(f'[+ {newPts} pts]')
            if product == "letters":
                playerObj.cargoManifest["letters"].remove(item)
            else:
                playerObj.cargoManifest["packages"].remove(item)
        return playerObj,True
    else:
        print('No items to deliver! Reloading cargo.')
        return playerObj, anySuccess
    
def leave(playerObj,planetObj):
    print(f"You are now leaving {playerObj.loc.nameL}.")
    planet_choice = get_planet_choice('Choose the number of the planet you would like to visit.',playerObj,planetObj)

    try:

        playerObj.loc = planet_choice
        return playerObj
    except IndexError:
        #Failed to fly?
        return playerObj

    