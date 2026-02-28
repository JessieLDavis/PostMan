from random import choice, choices
from assets.animations import *
from terminal_response import get_multiple_choice, get_planet_choice

def search(playerObj,planetClass):       
    # choice_range = range(30,step=2)
    num = choice(range(0,30,2))
    if num == 0:
        print("No deliverables found.")
        return 
    cargoSpace = playerObj.shipStats.get('cargoSpaceRemaining')
    if cargoSpace < num:
        print('Not enough space!')
        return
    destination = [plan for plan in planetClass.planet_dict.values() if plan != playerObj.loc]
    origin = playerObj.loc
    destination = choice(destination)
    product = choice(playerObj.loc.products)
    selection = (num,destination,product,origin)
    print(f'Loaded {num} {product} to deliver to {destination.nameL}')
    if playerObj.loc.nameL == "Post Office":
        playerObj.cargoManifest["letters"].append(selection)
    else:
        playerObj.cargoManifest["packages"].append(selection)
    playerObj.ship_cargo_set()
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
            print(f'[+ {newPts} units]')
            if product == "letters":
                playerObj.cargoManifest["letters"].remove(item)
            else:
                playerObj.cargoManifest["packages"].remove(item)
        playerObj.ship_cargo_set()
        return playerObj,True
    else:
        print('No items to deliver! Reloading cargo.')
        return playerObj, anySuccess
    
def leave(playerObj,planetObj,checkLaunch=True):
    if checkLaunch:
        launched = playerObj.ship_fuel_drain(1)
        if launched == False:
            return playerObj
    print(f"You are now leaving {playerObj.loc.nameL}.")
    planet_choice = get_planet_choice('Choose the number of the planet you would like to visit.',playerObj,planetObj)
    if playerObj.loc != planet_choice:
        opts = [planet_choice.navLoc,planet_choice.navLoc]
        dist = abs(max(opts) - min(opts))
        arrived = playerObj.ship_fuel_drain(dist)
        if arrived == False:
            print('Selected planet is too far at current fuel level.')
            return leave(playerObj,planetObj,False)
        
    try:
        playerObj.loc = planet_choice
        return playerObj
    except IndexError:
        #Failed to fly?
        return playerObj

def show_map(playerObj,planetObj):
    map_display(playerObj,planetObj)
    
def status(playerObj):
    print(playerObj.status())

def refuel(playerObj):
    # refuel_price
    fuelMax = playerObj.shipStats.get('fuelSpace')
    fuelRem = playerObj.shipStats.get('fuelRemaining')
    wallet = playerObj.points
    if fuelMax == fuelRem:
        print('Fuel already at max.')
        return playerObj
    fuelSlack = fuelMax-fuelRem
    baseCost = playerObj.loc.get_fuel_price()
    if baseCost == 0:
        print(f"Because of your continued efforts, the fuel tech was instructed to fill the fuel stores free of change.\n[ +{fuelSlack} blocks ] [ -0 units ]")
        playerObj.shipStats['fuelRemaining'] = fuelMax
        return playerObj
    percFul = playerObj.check_fuel(False)
    fuel_options = [.75,.5,.25]
    fuelSlack_100 = fuelSlack*baseCost
    fuel_choices = [["100",fuelSlack_100,fuelSlack]]
    fuel_dict = {"100":fuelSlack_100}
    for fl in fuel_options:
        if percFul <= fl:
            fuel_level = round(fuelMax*fl)*baseCost
            fuel_per = f"{fl*100}"
            # fuel_dict[fuel_per] = fuel_level
            fuelBlocks = (fuelMax*fl)-fuelRem
            fuel_choices.append([fuel_per,fuel_level,fuelBlocks])
    print(f'Current Units: {wallet}\t\tCurrent Fuel Level: {percFul*100}%')
    print(f'Current fuel cost is {baseCost} per block.')
    fuel_level = get_multiple_choice('How much fuel would you like to purchase?',[f"{fl[0]}% = {fl[1]}u" for fl in fuel_choices])
    fuel_level = fuel_level.split('%')[0]
    cost = fuel_dict.get(fuel_level)
    if cost == None:
        print('Not a valid fuel level.')
        return refuel(playerObj)
    elif cost > wallet:
        print('Not enough units.')
        return playerObj
    
    fuel_section = [sub for sub in fuel_choices if sub[0] == fuel_level][0]
    amount, price, blocks = fuel_section
    playerObj.shipStats['fuelRemaining'] += blocks
    playerObj.points -= price
    print(f'Fuel stores now at {amount}%\n[ +{blocks} blocks ] [ -{price} units ]')
    return playerObj


