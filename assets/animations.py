import time
import os
from nav_page import Planet
from player.player import Player
def launching():
    #https://www.asciiart.eu/ascii-night-sky-generator
    os.system('cls')
    nightsky ={
    "content": "            .               '            .                                      \n .  .                        .                                 '     '          \n            .                        '+                                         \n                                                                                \n                                        o                      .                \n                                                 +     +                        \n        .                                                  .                    \n     .                                                                          \n'                               '                    o                  '       \n                                                 .          *                   \n                                         .                                      \n                                                         .   '                  \n                           +                                                    \n                     .    '                           o                   o     \n                                                                     +     .    \n                                                                     .          \n                   .                                                            \n                                                                              * \n                         .                                              *     + \n                +           o                                                   ",
    "width": 80,
    "height": 20,
    "created": "2026-02-25T03:07:17.520Z",
    "software": "ASCII Art Archive (asciiart.eu)"
    }
    nightsky_content = nightsky.get('content')
    print(nightsky_content)
    nightsky_content = nightsky_content.split('\n')
    width = nightsky.get('width')
    height = nightsky.get('height')
    # for n in nightsky_content:
    frames = 8
    cap = 7
    for x in range(frames):
        ship = '<-[ooo]->'
        if x != 0 and x <= cap:
            ship_row = nightsky_content[-x]
            ship_row = [char for char in ship_row]
            ship_row[35:44] = ship
            ship_row = ''.join(ship_row)
            nightsky_content[-x] = ship_row
        elif x >= cap:
            ship_row = nightsky_content[-cap]
            ship_row = [char for char in ship_row]
            ship_row[35:44] = ship
            ship_row = ''.join(ship_row)
            nightsky_content[-cap] = ship_row
        nightsky_content = '\n'.join(nightsky_content)
        os.system('cls')
        print(nightsky_content)
        # print('-----'*10)
        time.sleep(.2)
        
        nightsky_content = nightsky.get('content').split('\n')

def landing():
    #https://www.asciiart.eu/ascii-night-sky-generator
    os.system('cls')
    nightsky ={
    "content": "_|_                      .           '                                  o       \n |                .                      '                                      \n                              +                   _|_     '                   . \n                               .                   |                            \n                  *                             o            +                  \n    _|_             '                                                           \n '   |                                                           .      .    o  \n                                                    *        '                  \n                                                                                \n                 .                                                              \n         *                              '       '      '                        \n.                                                                               \n                                                                                \n                             ' .     *                                          \n         *                                                                      \n                                                                                \n                                                                                \n':, ,','., ,:':, ,','., ,:':,                     ,:':, ,','., ,:':, ,','., ,:'\n,','., ,:':, ,','., ,:':, ,','.,               ,','., ,:':, ,','., ,:':, ,','.,\n---------------------------------_____________---------------------------------",
    "width": 80,
    "height": 20,
    "created": "2026-02-25T03:25:02.268Z",
    "software": "ASCII Art Archive (asciiart.eu)"
    }
    nightsky_content = nightsky.get('content')
    print(nightsky_content)
    nightsky_content = nightsky_content.split('\n')
    width = nightsky.get('width')
    height = nightsky.get('height')
    # for n in nightsky_content:
    frames = 8
    cap = 7
    for x in range(height):
        ship = '<-[ooo]->'
        if  x < height:
            ship_row = nightsky_content[x]
            ship_row = [char for char in ship_row]
            ship_row[35:44] = ship
            ship_row = ''.join(ship_row)
            nightsky_content[x] = ship_row
        elif x == height:
            ship_row = nightsky_content[-1]
            ship_row = [char for char in ship_row]
            ship_row[35:44] = ship
            ship_row = ''.join(ship_row)
            nightsky_content[-1] = ship_row
        nightsky_content = '\n'.join(nightsky_content)
        os.system('cls')
        print(nightsky_content)
        # print('-----'*10)
        time.sleep(.2)
        
        nightsky_content = nightsky.get('content').split('\n')

def map_display(playerObj:Player=None,planet_obj:Planet=None):
    os.system('cls')
    if playerObj != None:
        current_loc = playerObj.loc
    else:
        current_loc = None
    # map_content = {
    # "content": "  .                                                                           \n                          .           .-.     .-.                     .-.     \n                                     (   )   (   )                   (   )    \n        '                   *         `-'     `-'  o                  `-'     \n                                                                              \n                                                                              \n                                                                       '      \n                                                                              \n                                                                              \n    .-.                |        ':.                                           \n   (   )   .-.       - o -        '::._                                       \n    `-'   (   )        |            '._)            .-.                       \n           `-'                                     (   )                      \n                                                    `-'             .-.       \n                      .-.                       +                  (   )      \n                     (   )                                          `-'   .-. \n                      `-'                                                (   )\n                                                                          `-' ",
    # "width": 78,
    # "height": 18,
    # "created": "2026-02-25T04:17:26.843Z",
    # "software": "ASCII Art Archive (asciiart.eu)"
    # }
    map_str = """
    \n╔─────────────────────────────────────────────────────────────────────────────────────╗\n|  .                                                                [ABORIA]   |\n|                          .                   .-.                     .-.     |\n|          [FLORENCE]                         (   )                   (   )    |\n|        '     .-.           *                 `-'  o                  `-'     |\n|             (   )                           [IDA]                            |\n|              `-'                                                             |\n|                                                                       '      |\n|                                                                              |\n| [LOOGONIA]                      .                                            |\n|    .-.                _|       ':.                                           |\n|   (   )   .-.        |o|         '::._         [METROCITY]                   |\n|    `-'   (   )        ||           '._)            .-.                       |\n|           `-'       [POST]      [ROCKY'S]         (   )       [VICTORY]      |\n|        [MUSTAFAR]  [OFFICE]    [ROCKET SHOP]       `-'           .-.         |\n|                      .-.                       +                (   )        |\n|                     (   )                                        `-'         |\n|                      `-'                                                     |\n|                   [GARDENIA]                                                 |\n╚──────────────────────────────────────────────────────────────────────────────────────╝
    """
    print(map_str)
    if current_loc != None:
        print(f"Current location: {current_loc.nameL}")

def unload_cargo(letters_to_unload=0,packages_to_unload=0):
    ship_line = "---------------------------------__<-[ooo]->__---------------------------------"

def pyramid(amount,baseLayer=20):
    row_cts = []
    amount = amount
    while amount> baseLayer:
        row_cts.append(baseLayer)
        amount -= baseLayer
    nextLayer = baseLayer
    while amount > 0 and nextLayer>0:
        nextLayer = baseLayer-2
        if amount >= nextLayer:
            row_cts.append(nextLayer)
            amount -= nextLayer
        else:
            pass
    row_cts.append(amount)
    row_cts.sort(reverse=True)
    return row_cts



def load_cargo(letters_to_unload=0,packages_to_unload=0):
    ship_line = "---------------------------------__<-[ooo]->__---------------------------------"
    if letters_to_unload>0:
        letter_rows = pyramid(letters_to_unload)
    else:
        letter_rows = []

    if packages_to_unload>0:
        package_rows = pyramid(packages_to_unload)
    else:
        package_rows = []
        
    package = '[]'
    letter = '/'

    # load packages from left and letters from right

    

            



def test_animations():

    print('Launching:')
    launching()
    input('---'*10)
    print('Landing:')
    landing()
    input('---'*10)
    print('Unloading:')
    unload_cargo()
    input('---'*10)
    print('Loading:')
    load_cargo()
    input('---'*10)

    return

# test_animations()

"':, ,','., ,:':, ,','., ,:':,                     ,:':, ,','., ,:':, ,','., ,:'"
",','., ,:':, ,','., ,:':, ,','.,               ,','., ,:':, ,','., ,:':, ,','.,"
"---------------------------------_____________---------------------------------"


"╔─────────────────────────────────────────────────────────────────────────────────────╗"
"|  .                                                                [ABORIA]   |"
"|                          .                   .-.                     .-.     |"
"|          [FLORENCE]                         ( 5 )                   ( 1 )    |"
"|        '     .-.           *                 `-'  o                  `-'     |"
"|             ( 8 )                           [IDA]                            |"
"|              `-'                                                             |"
"|                                                                       '      |"
"|                                                                              |"
"| [LOOGONIA]                      .                                            |"
"|    .-.                _|       ':.                                           |"
"|   ( 2 )   .-.        |o|         '::._         [METROCITY]                   |"
"|    `-'   ( 6 )        ||           '._)            .-.                       |"
"|           `-'       [POST]      [ROCKY'S]         ( 3 )       [VICTORY]      |"
"|        [MUSTAFAR]  [OFFICE]    [ROCKET SHOP]       `-'           .-.         |"
"|                      .-.                       +                ( 7 )        |"
"|                     ( 4 )                                        `-'         |"
"|                      `-'                                                     |"
"|                   [GARDENIA]                                                 |"
"╚──────────────────────────────────────────────────────────────────────────────────────╝"

# static   Post Office   0
#   east   Aboria   1
# west   Loogonia   2
#   east   MetroCity   3
# west   Gardenia   4
#   east   Ida   5
# west   Mustafar   6
#   east   Victory   7
# west   Florence   8
#   east   Rusty's Rocket Shop   9

"                         [][][]                                                "
"                        [][][][]               ,,,,,,,,,,,,                    "
"---------------------------------__<-[ooo]->__---------------------------------"