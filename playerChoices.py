from random import choice,choices
from assets import animations

def search(playerObj,planetList):
    num = choice(range(30,2))
    if num == 0:
        print("No packages found.")
        return playerObj
    destination = [plan for plan in planetList if plan != playerObj.loc]
    destination - choice[destination]
    product = choice[playerObj.loc.products]
    selection = (num,destination,product)
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
        for item in deliverList:
            number, destination, product = item
            playerObj.loc.playerImpact += number
            playerObj.points += (number*10)
            destination.playerImpact += number
            if product == "letters":
                playerObj.cargoManifest["letters"].remove(item)
            else:
                playerObj.cargoManifest["packages"].remove(item)
        return deliver(playerObj,True)
    else:
        return playerObj, anySuccess
def leave(playerObj,planetList):
    planetOptionsSplit = int((len(planetList)-2)/2)+1
    planetListMinus = [planet for planet in planetList if planet.loc.nameL != "Rusty's Rocket Shop"]
    if playerObj.loc.nameL == "Post Office" or playerObj.loc.nameL == "Rusty's Rocket Shop":
        # planetOptions = [planet for planet in planetList if planet != playerObj.loc]
        planetOptions = [planet for planet in planetListMinus if planet != playerObj.loc]
    else:
        planetOptionsWest = planetList[:planetOptionsSplit]
        planetOptionsEast = planetList[planetOptionsSplit:]
        if playerObj.loc in planetOptionsWest:
            planetOptions = planetOptionsWest
        else:
            planetOptions = planetOptionsEast
        planetOptions.append(planetList[0])
        # planetOptionsWest.append(planetList[0])
        # planetOptionsEast.append(planetList[0])
    rockyShows = choices([True,False],[1,4])
    rocky = [planet for planet in planetList if planet.nameL == "Rusty's Rocket Shop"][0]
    if rockyShows == True and playerObj.loc.nameL !="Rusty's Rocket Shop":
        planetOptions.append(rocky)
    print(f"You are now leaving {playerObj.loc.nameL}.")
    for planetObj in planetOptions:
        print(planetObj.showLoc(),end=" | ")
    planetChoice =input("Choose the number of the planet you would like to visit.\n>  ")
    try:
        planetList[int(planetChoice)]
        playerObj.loc = planetList[int(planetChoice)]
        return playerObj
    except IndexError:
        #Failed to fly
        return playerObj

    