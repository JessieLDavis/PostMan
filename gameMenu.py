import json, os
import random
from nav_page import Planet
from player.player import Player
from terminal_response import get_multiple_choice

# self,navLoc,name,description,economy=None,products=None,population=None,fluidCapital=None
def create_planets(planetList=None):
    if planetList == None:
        planetList = [
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

    pList = []
    for i, listObj in enumerate(planetList):
        # listObj = i
        planetObj = Planet(i,*listObj)
        pList.append(planetObj)
    return pList

def create_player(jsonSave=None):
    if jsonSave != None:
        loc,points,title,cargoManifest,shipStats = jsonSave
    else:
        loc = None
        points = 0
        title = "Citizen"
        cargoManifest = {"letters":[],"packages":[]}
        shipStats = {"cargoSpace":50,"cargoSpaceRemaining":50,"speed":50,"durability":50,"fuelSpace":50,"fuelRemaining":50}
    playerObj = Player(loc,points,title,cargoManifest,shipStats)
    return playerObj


def setPlanets(jsonSave=None):
    if jsonSave != None:
        planetList = jsonSave["planetList"]
        #load from save
    else:
        planetList = None
    return create_planets(planetList)
    # return planetList
        #take planets from planets json

def setPlayer(jsonSave=None):
    if jsonSave != None:
        playerObj = jsonSave["playerObj"]
    else:
        playerObj = None
    return create_player(playerObj)
    # return playerObj

def load_save(playerSave):
    # with open(playerSave,"r") as loading:
    loadedFile = json.load(playerSave)
    return [setPlayer(loadedFile),setPlanets(loadedFile)]


def new_game():
    return [setPlayer(),setPlanets()]

def save_game(playerSave,playerObj,planetList):
    # playerSave = "player/player_save.json"
    # planetSave = "assets/planets.json"

    # planetReport = [p.data for p in planetList]
    saveFile = {
        "playerObj":[
            playerObj.loc,
            playerObj.points,
            playerObj.title,
            playerObj.cargoManifest,
            playerObj.shipStats
        ],
        "planetList":(
            [p.data for p in planetList]
        )
    }
    try:
        with open(playerSave,"w") as saving:
            json.dump(saveFile,saving)
        return "Game Saved"
    except IndexError:
        return "Problem Saving Game"

def game_menu():
    playerSave = "player/player_save.json"
    # planetSave = "assets/planets.json"
    choices = ["New Game","Load Game"]
    #input to select menu item
    userChoice = get_multiple_choice('',choices,add_other=True,other_text='Back')
    # userChoice = input(f"{choices[0]}\n{choices[1]}\n>  ")
    if userChoice == 'New Game':
        return new_game()
    elif userChoice == 'Load Game':
        return load_save(playerSave)
    elif userChoice == 'Back':
        return None
    else:
        #invalid choice
        return game_menu()
