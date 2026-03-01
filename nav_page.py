#nav menu
from random import choice,choices
class Planet():
    planet_dict = {}
    planet_west = []
    planet_east = []
    post_office = None
    gas_station = {}

    def __init__(self,navLoc,name,description,economy=0,products=['packages'],population=0,fluidCapital=0,planetRelations:dict={},space_location:str='static',playerImpact:int=0):
        self.navLoc:int = navLoc
        self.nameL:str = name
        self.description:str = description
        self.economy:int = economy
        self.products:list = products
        self.population:int = population
        self.fluidCapital:int = fluidCapital
        self.planetRelations:dict = planetRelations
        self.space_location:str = space_location
        # self.likes:dict = needs
        # self.hates:dict = hates
        self.playerImpact:int = playerImpact
        # Planet.planet_list[self.nameL] = self

        # if self.economy == None:
    def __str__(self):
        return f"{self.nameL}: {self.description}\n{self.products}"
    
    def data(self):
        return [self.navLoc,self.nameL,self.description,self.economy,self.products,self.population,self.fluidCapital,self.planetRelations,self.space_location,self.playerImpact]
    
    def welcomeMsg(self):
        return f"[{self.nameL}]\n{self.description}"
    
    def showLoc(self):
        return f"{self.navLoc} - {self.nameL}"
    
    @classmethod
    def get_planets(cls,side:str='all',includeGas:bool=False,onlyNames:bool=False):
        if onlyNames:
            if side == 'all':
                planet_list = list(cls.planet_dict.keys())
            elif side == 'west':
                planet_list = [o.nameL for o in cls.planet_west]
                planet_list.append(cls.post_office.nameL)
            elif side == 'east':
                planet_list = [o.nameL for o in cls.planet_east]
                planet_list.append(cls.post_office.nameL)
            if includeGas:
                gasOption = choice(list(cls.gas_station.keys()))
                planet_list.append(gasOption)
            else:
                for name, station in cls.gas_station.items():
                    if name in planet_list:
                        planet_list.remove(name)
        else:
            if side == 'all':
                planet_list = list(cls.planet_dict.values())
            elif side == 'west':
                planet_list = [o for o in cls.planet_west]
                planet_list.append(cls.post_office)
            elif side == 'east':
                planet_list = [o for o in cls.planet_east]
                planet_list.append(cls.post_office)
            if includeGas:
                gasOption = choice(list(cls.gas_station.values()))
                planet_list.append(gasOption)
            else:
                for name, station in cls.gas_station.items():
                    if station in planet_list:
                        planet_list.remove(station)
        return planet_list
        

    @classmethod
    def select_planet(cls,planet_name):
        selectedPlanet = cls.planet_dict.get(planet_name)
        if selectedPlanet == None:
            print('Planet not found')
            return cls.select_planet(planet_name)
        return selectedPlanet
    
    @classmethod
    def create_map(cls,planet_seed:list=None):
        if planet_seed == None:
            planet_seed = [
                ["Post Office","Welcome to the Intergalactic Post Office! This is the hub of all letters to be delivered.",0,["letters"]],
                ["Aboria","Welcome to the beautiful land of Aboria! We specializze in creating products from our deep forest.",None,["stacks of lumber","crates of paper","paper fans","acorn bundles"]],
                ["Loogonia","Welcome to Loogonia where sea stretches as far as the eye can see.",None,["crates of fish","barrels of salt water","salt cakes","jugs of desalinated water","fishing poles","crates of dried seaweed"]],
                ["MetroCity","Welcome to the halogen hub of the known universe! All the best and brightest find their way here to MetroCity.",3,["entertainment discs","crates of books","textbooks","musical instruments","scholarly journals","sculptures"]],
                ["Gardenia","Welcome to the flower garden, Gardenia. Would you like some herbs for your ship?",None,["bushels of flowers","baskets of rose pedals","crates of medicinal herbs","insect repellant","bouquets","jars of honey"]],
                ["Ida","Welcome to the Ida where most of the galactic food comes from. Enjoy your stay!",None,["bushels of wheat","corn bushels","sacks of flour","bags of sunflower seeds","crates of cured meat","fertilizer bags","jars of honey","bars of soap"]],
                ["Mustafar","Careful! Welcome to the last port of safety in the firestorm. Be careful on Mustafar and you'll get out fine.",None,["evil plans","crates of charcoal","obsidian blocks"]],
                ["Victory","Welcome to the busiest spot in the greater Galactic way. Victory is the place to be!",None,["crates of shoes","boxes of gambling wins","sports memorabilia","game winning pucks","sports jerseys"]],
                ["Florence","Welcome to the fashion show. All the clothes you may desire is found in Florence.",3,["fabric bolts","linen dresses","crates of shoes","boxes of necklaces","billowy shirts","cotton bolts"]],
                ["Rusty's Rocket Shop","Welcome to the my traveling repair shop! Rusty's Rocket Shop is swinging by and can do everything except stop!",0,["lost packages","dead letters","nuts and bolts"]]
            ]
        # else:


        # pList = []
        isWest = False
        for i, listObj in enumerate(planet_seed):
            # listObj = i
            planetObj = Planet(i,*listObj)
            if ' Shop' in planetObj.nameL:
                planetObj.space_location = 'mystery'
                Planet.gas_station[planetObj.nameL] = planetObj
            else:
                Planet.planet_dict[planetObj.nameL] = planetObj
                if planetObj.nameL.startswith('Post Office'):
                    planetObj.space_location = 'static'
                    Planet.post_office = planetObj
                elif isWest:
                    planetObj.space_location = 'west'
                    Planet.planet_west.append(planetObj)
                    isWest = False
                else:
                    planetObj.space_location = 'east'
                    Planet.planet_east.append(planetObj)
                    isWest = True
            # print(planetObj.space_location,' ',planetObj.nameL," ",planetObj.navLoc)
        # print([f"{p.nameL}: {p.space_location} {p.navLov}" for p in Planet.planet_dict.values()])
        return Planet
    
    def get_fuel_price(self):
        #price per block. should be relatively cheap for now?
        gas_station = Planet.gas_station.get(self.nameL,False)
        if gas_station == False:
            basePrice = 300 - (self.playerImpact/1000)
        else:
            #gas prices cheaper from station in the short term but might not be better in long
            basePrice = 50
        if basePrice < 0:
            basePrice = 0
        else:
            basePrice = round(basePrice,0)
        return basePrice

    @classmethod
    def get_gossip(cls,playerPlanet):
        # check planetary relations
        pass

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
    
