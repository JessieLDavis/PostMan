import time
import os
# from nav_page import Planet
# from player.player import Player
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
        time.sleep(.02)
        
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
        time.sleep(.02)
        
        nightsky_content = nightsky.get('content').split('\n')

def map_display(playerObj=None,planet_obj=None):
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

# def unload_cargo(letters_to_unload=0,packages_to_unload=0):
#     ship_line = "---------------------------------__<-[ooo]->__---------------------------------"

def pyramid(amount,baseLayer=15):
    row_cts = []
    amount = amount
    while amount> baseLayer:
        row_cts.append(baseLayer)
        amount -= baseLayer
    nextLayer = baseLayer
    lastLayer = baseLayer
    while amount > 0 and nextLayer>0:
        nextLayer = lastLayer-2
        if amount >= nextLayer:
            row_cts.append(nextLayer)
            amount -= nextLayer
        else:
            pass
        lastLayer = nextLayer
    row_cts.append(amount)
    row_cts.sort(reverse=True)
    return row_cts



def view_cargo(letter_amount=0,package_amount=0):
    ship_line = "---------------------------------__<-[ooo]->__---------------------------------"
    # os.system('cls')
    if letter_amount>0:
        letter_rows = pyramid(letter_amount)
    else:
        letter_rows = []

    if package_amount>0:
        package_rows = pyramid(package_amount)
    else:
        package_rows = []
        
    package = '[]'
    letter = '/'
    longest_side = max(len(package_rows),len(letter_rows))
    
    # load packages from left and letters from right
    row_list = []
    for ind in range(longest_side):
        base = '                                 '
        row_str = []
        try:
            p = package_rows[ind]
            p = p*package
            p = f"{(len(base)-len(p))*' '}{p}"
        except IndexError:
            p = base

        row_str.append(p)

        #add mid
        mid = f"{" "*13}"
        row_str.append(mid)

        try:
            l = letter_rows[ind]
            l = l*letter
            l = f"{l}{(len(base)-len(l))*' '}"
        except IndexError:
            l = base
        row_str.append(l)

        row_str = ''.join(row_str)
        row_list.append(row_str)
    row_list.reverse()
    row_list.append(ship_line)
    row_list = '\n'.join(row_list)
    print(row_list)


def unload_cargo(letters_to_unload=0,packages_to_unload=0):
    os.system('cls')
    if letters_to_unload == 0 and packages_to_unload == 0:
        view_cargo()
    else:
        while letters_to_unload>0 and packages_to_unload>0:
            os.system('cls')
            view_cargo(letters_to_unload,packages_to_unload)
            if letters_to_unload!=0:
                letters_to_unload -=1
            if packages_to_unload != 0:
                packages_to_unload -= 1
            time.sleep(1)
    return

def load_cargo(letters_to_load=0,packages_to_load=0):
    os.system('cls')
    if letters_to_load == 0 and packages_to_load == 0:
        view_cargo()
    else:
        while letters_to_load>0 and packages_to_load>0:
            os.system('cls')
            view_cargo(letters_to_load,packages_to_load)
            if letters_to_load!=0:
                letters_to_load -=1
            if packages_to_load != 0:
                packages_to_load -= 1
            time.sleep(1)
    return

            



def test_animations():

    print('Launching:')
    launching()
    input('-'*80)
    print('Landing:')
    landing()
    input('-'*80)
    print('Unloading:')
    unload_cargo()
    input('-'*80)
    unload_cargo(10,10)
    input('-'*80)
    unload_cargo(50,10)
    input('-'*80)
    unload_cargo(10,50)
    input('-'*80)
    unload_cargo(1,5)
    input('-'*80)
    print('Loading:')
    load_cargo()
    input('-'*80)
    load_cargo(10,10)
    input('-'*80)
    load_cargo(50,10)
    input('-'*80)
    load_cargo(10,50)
    input('-'*80)
    load_cargo(5,1)
    input('-'*80)

    return

test_animations()

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