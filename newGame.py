import json, os
import random
from nav_page import Planet

# self,navLoc,name,description,economy=None,products=None,population=None,fluidCapital=None
def create_planets():
    planetList = [
        ["Post Office","Welcome to the Intergalactic Post Office! This is the hub of all letters to be delivered.",0],
        ["Aboria","Welcome to the beautiful land of Aboria! We specializze in creating products from our deep forest.",None,["stacks of lumber","crates of paper","paper fans","acorn bundles"]],
        ["Loogonia","Welcome to Loogonia where sea stretches as far as the eye can see.",None,["crates of fish","barrels of salt water","salt cakes","jugs of desalinated water","fishing poles","crates of dried seaweed"]],
        ["MetroCity","Welcome to the halogen hub of the known universe! All the best and brightest find their way here to MetroCity.",3,["entertainment discs","crates of books","textbooks","musical instruments","scholarly journals","sculptures"]],
        ["Gardenia","Welcome to the flower garden, Gardenia. Would you like some herbs for your ship?",None,["bushels of flowers","baskets of rose pedals","crates of medicinal herbs","insect repellant","bouquets","jars of honey"]],
        ["Ida","Welcome to the Ida where most of the galactic food comes from. Enjoy your stay!",None,["bushels of wheat","corn bushels","sacks of flour","bags of sunflower seeds","crates of cured meat","fertilizer bags","jars of honey","bars of soap"]],
        ["Mustafar","Careful! Welcome to the last port of safety in the firestorm. Be careful on Mustafar and you'll get out fine.",None,["evil plans","crates of charcoal","obsidian blocks"]],
        ["Victory","Welcome to the busiest spot in the greater Galactic way. Victory is the place to be!",None,["crates of shoes","boxes of gambling wins","sports memorabilia","game winning pucks","sports jerseys"]],
        ["Florence","Welcome to the fashion show. All the clothes you may desire is found in Florence.",3,["fabric bolts","linen dresses","crates of shoes","boxes of necklaces","billowy shirts","cotton bolts"]],
        ["Rusty's Rocket Shop","Welcome to the my traveling repair shop! Rusty's Rocket Shop is swinging by and can do everything except stop!",0]
    ]
    pList = []
    for i in range(planetList):
        listObj = planetList[i]
        planetObj = Planet(i,*listObj)
        pList.append(planetObj)



def setPlanets(jsonSave=None):
    if jsonSave != None:
        #load from save
        pass
    else:
        pass
        #take planets from planets json

