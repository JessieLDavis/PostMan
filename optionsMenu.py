import json

optionsFile = "assets/options.json"

def options_menu():
    optionsFile = "assets/options.json"
    with open(optionsFile,"r+b") as optFile:
        oP = json.load(optFile)
    options = {
        "Difficulty":["Easy","Normal","Hard"],
        "Player Color":["Green","White","Red","Blue"],
        "Travel Time": [True,False],
        "Auto-deliver": [True,False],
        "Speedrunner Mode": [True,False]
    }
    confirmFinish = False
    while confirmFinish != True:
        userSelect = input("Option Select")
        try:
            options[userSelect]
            optionChoice = options[userSelect]
            userSet = input("Option set")
            # with open(optionsFile,"r+b") as optionFile:
            #     json.lo
            oP[userSelect] = userSet
        except IndexError:
            # print("Invalid choice.")
            confirmFinish = True
    with open(optionsFile,"w") as opDrop:
        json.dump(oP,opDrop)
    return oP

 