from random import choice, choices
from assets.animations import *
from assets.screens import show_sub_menu
from assets.terminal_response import get_multiple_choice, get_planet_choice


def search(playerObj,planetClass):
    str_list = show_sub_menu(playerObj,add_delay=True,delayStr="Searching for deliverables")
    playerObj.message = ''   
    # str_path = ["Searching for deliverables."]
    num = choice(range(0,30,2))
    if num == 0:
        # str_list.append('No deliverables found.')
        show_sub_menu(playerObj,messageStr="No deliverables found.",last_str=str_list)
        playerObj.message = f"No deliverables found in search."
        time.sleep(1)
        return 
    else:
        str_list = show_sub_menu(playerObj,messageStr=f"{num} packages found.",last_str=str_list)
    cargoSpace = playerObj.shipStats.get('cargoSpaceRemaining')
    if cargoSpace < num:
        str_list = show_sub_menu(playerObj,messageStr=f"Not enough space in cargo hold!",last_str=str_list)
        playerObj.message = 'Cargo was not loaded due to capacity.'
        time.sleep(1)
        return
    
    destination = [plan for plan in planetClass.planet_dict.values() if plan != playerObj.loc]
    origin = playerObj.loc
    destination = choice(destination)
    product = choice(playerObj.loc.products)
    selection = (num,destination,product,origin)
    str_list = show_sub_menu(playerObj,messageStr=f'Loaded {num} {product} to deliver to {destination.nameL}',last_str=str_list)
    playerObj.message = f'Loaded {num} {product} to deliver to {destination.nameL}'

    if playerObj.loc.nameL == "Post Office":
        playerObj.cargoManifest["letters"].append(selection)
    else:
        playerObj.cargoManifest["packages"].append(selection)
    playerObj.ship_cargo_set()
    return playerObj

def deliver(playerObj,anySuccess=False):
    
    playerObj.message = ''
    letterList = [plan for plan in playerObj.cargoManifest["letters"] if plan[1] == playerObj.loc]
    packageList = [plan for plan in playerObj.cargoManifest["packages"] if plan[1] == playerObj.loc]
    deliverList = letterList + packageList
    str_list = show_sub_menu(playerObj,"",delayStr="Unloading cargo",add_delay=True)
    if len(deliverList) != 0:
        totalDelivered = 0
        totalProfit = 0
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
            
            
            inter = "-"*WIDTH
            foundCargo =f'{number} {product} delivered!'
            pts = f'[+ {newPts} units]'
            for x in [inter,foundCargo,pts]:
                str_list = show_sub_menu(playerObj,x,str_list)
            if anySuccess == False:
                anySuccess = True
            # playerObj.message = f'{number} {product} delivered!  [+ {newPts} units]'
            totalDelivered += number
            totalProfit += newPts
            if product == "letters":
                playerObj.cargoManifest["letters"].remove(item)
            else:
                playerObj.cargoManifest["packages"].remove(item)
        playerObj.message = f"{totalDelivered} delivered. [ + {totalProfit} units]"
        playerObj.ship_cargo_set()
        # return playerObj,True
    else:
        # print('No items to deliver! Reloading cargo.')
        str_list = show_sub_menu(playerObj,'No deliverables for this location in hold!',str_list,"Reloading cargo",True)
        # time.sleep(1)
        playerObj.message = 'No items to deliver.'

    time.sleep(1)
    return playerObj, anySuccess
    
def leave(playerObj,planetObj,checkLaunch=True):
    playerObj.message = ''
    str_list = show_sub_menu(playerObj,delayStr="Starting engine",add_delay=True)
    if checkLaunch:
        launched = playerObj.ship_fuel_drain(1)
        if launched == False:
            str_list = show_sub_menu(playerObj,"Not enough fuel to launch!",delayStr="Talking to Port Authority",delay_amount=5,add_delay=True)
            str_list = show_sub_menu(playerObj,f"Cleared to stay on {playerObj.loc.nameL} longer.")
            playerObj.message = "Not enough fuel to launch."
            return playerObj
    str_list = show_sub_menu(playerObj,f"You are now leaving {playerObj.loc.nameL}.",str_list)
    # print()
    planet_choice = get_planet_choice('Choose the number of the planet you would like to visit.',playerObj,planetObj)
    if playerObj.loc != planet_choice:
        opts = [planet_choice.navLoc,planet_choice.navLoc]
        dist = abs(max(opts) - min(opts))
        arrived = playerObj.ship_fuel_drain(dist)
        if arrived == False:
            print('Selected planet is too far at current fuel level.')
            time.sleep(1)
            return leave(playerObj,planetObj,False)
        
    try:
        playerObj.loc = planet_choice
        return playerObj
    except IndexError:
        #Failed to fly?
        return playerObj

def show_map(playerObj,planetObj):
    playerObj.message = map_display(playerObj,planetObj)
    
def get_player_status(playerObj):
    # print(f"\n\n{playerObj}\n")
    # print(playerObj.all_status())
    # playerObj.message = playerObj.all_status()
    pass
    return playerObj

def refuel(playerObj):
    # refuel_price
    fuelMax = playerObj.shipStats.get('fuelSpace')
    fuelRem = playerObj.shipStats.get('fuelRemaining')
    wallet = playerObj.points
    if fuelMax == fuelRem:
        print('Fuel already at max.')
        time.sleep(1)
        return playerObj
    fuelSlack = fuelMax-fuelRem
    baseCost = playerObj.loc.get_fuel_price()
    if baseCost == 0:
        print(f"Because of your continued efforts, the fuel tech was instructed to fill the fuel stores free of change.\n[ +{fuelSlack} blocks ] [ -0 units ]")
        playerObj.message = f"Because of your continued efforts, the fuel tech was instructed to fill the fuel stores free of change.\n[ +{fuelSlack} blocks ] [ -0 units ]"
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
    playerObj.message = f'Current fuel cost is {baseCost} per block.'
    # price_list = 
    fuel_level = get_multiple_choice('How much fuel would you like to purchase?',[f"{fl[0]}% for {fl[1]}u" for fl in fuel_choices],add_other=True,other_text=
    'Cancel')
    if fuel_level == 'Cancel':
        return playerObj
    fuel_level = fuel_level.split('%')[0]
    cost = fuel_dict.get(fuel_level)
    if cost == None:
        print('Not a valid fuel level.')
        time.sleep(1)
        return refuel(playerObj)
    elif cost > wallet:
        print('Not enough units.')
        time.sleep(1)
        return playerObj
    
    fuel_section = [sub for sub in fuel_choices if sub[0] == fuel_level][0]
    amount, price, blocks = fuel_section
    playerObj.shipStats['fuelRemaining'] += blocks
    playerObj.points -= price
    playerObj.message = f'Fuel stores now at {amount}%\n[ +{blocks} blocks ] [ -{price} units ]'
    return playerObj

def influence(playerObj):
    print(f"Current impact for {playerObj.loc.nameL}: {playerObj.loc.playerImpact}")
    return

def evesdrop(playerObj,planetObj):
    # call planet gossip?
    pass