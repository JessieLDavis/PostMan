#nav menu
from random import choice,choices
class Planet():
    def __init__(self,navLoc,name,description,economy=None,products=None,population=None,fluidCapital=None,planetRelations:dict=None,playerImpact:int=0):
        self.navLoc:int = navLoc
        self.nameL:str = name
        self.description:str = description
        self.economy:int = economy
        self.products:list = products
        self.population:int = population
        self.fluidCapital:int = fluidCapital
        self.planetRelations:dict = planetRelations
        # self.likes:dict = needs
        # self.hates:dict = hates
        self.playerImpact:int = playerImpact

        # if self.economy == None:
    def __str__(self):
        return f"{self.nameL}: {self.description}\n{self.products}"
    def data(self):
        return [self.navLoc,self.nameL,self.description,self.economy,self.products,self.population,self.fluidCapital,self.playerImpact]
    def welcomeMsg(self):
        return f"[{self.nameL}]\n{self.description}"
    def showLoc(self):
        return f"{self.navLoc}: {self.nameL}"
    
# def search(playerObj,planetList):
#     num = choice(range(30,2))
#     if num == 0:
#         print("No packages found.")
#         return playerObj
#     destination = [plan for plan in planetList if plan != playerObj.loc]
#     destination - choice[destination]
#     product = choice[playerObj.loc.products]
#     selection = (num,destination,product)
#     if playerObj.loc.nameL == "Post Office":
#         playerObj.cargoManifest["letters"].append(selection)
#     else:
#         playerObj.cargoManifest["packages"].append(selection)
#     return playerObj
# def deliver(playerObj,anySuccess=False):
#     letterList = [plan for plan in playerObj.cargoManifest["letters"] if plan[1] == playerObj.loc]
#     packageList = [plan for plan in playerObj.cargoManifest["packages"] if plan[1] == playerObj.loc]
#     deliverList = letterList + packageList
#     if len(deliverList) != 0:
#         for item in deliverList:
#             number, destination, product = item
#             playerObj.loc.playerImpact += number
#             playerObj.points += (number*10)
#             destination.playerImpact += number
#             if product == "letters":
#                 playerObj.cargoManifest["letters"].remove(item)
#             else:
#                 playerObj.cargoManifest["packages"].remove(item)
#         return deliver(playerObj,True)
#     else:
#         return anySuccess
    
