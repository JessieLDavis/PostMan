import time
def launching():
    for x in range(10):
        if x%3 == 0:
            print(' '*50)
            print("      .   "*5)
            print(' '*50)
            print("  *       "*6)
        elif x%4 == 0:
            print("  '    "*9)
            # print("     *    "*5)
        else:
            print("   '      "*4)
            print(' '*50)
            print("       .  "*6)
            print(' '*50)
        time.sleep(.1)

def landing():
    pass

def map_display():
    pass

def unload_cargo():
    pass

def load_cargo():
    pass

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

test_animations()