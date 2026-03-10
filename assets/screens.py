import os
import time
from assets.screen_settings import HEIGHT,WIDTH,FRAME_RATE



def show_menu(playerObj,justLanded:bool=False):
    os.system('cls')
    if justLanded:
        # add landing animation
        menuStr = f"""  
    [{playerObj.loc.nameL}]\n{playerObj.loc.description}\n\n{playerObj.cargo}\n
    """
    else:
       menuStr = f"""  
    [{playerObj.loc.nameL}]\n{playerObj.message}\n\n{playerObj.cargo}\n
    """ 
    print(menuStr)
    return

def show_sub_menu(playerObj,messageStr:str="",last_str:list=[],delayStr:str="Processing",add_delay:bool=False,delay_amount:int=3):
    os.system('cls')
    str_list = [f"[{playerObj.loc.nameL} / {playerObj.lastChoice}]"]
    last_str.append(messageStr)
    last_str = reformat_str(last_str)
    last_str = limit_height(last_str,add_delay)
    # if len(last_str)> HEIGHT
    str_list.extend(last_str)
    
    message = '\n'.join(str_list)
    print(message)
    
    if add_delay:
        print()
        for sec in range(delay_amount):
            print(delayStr,f"."(sec+1),end="\r")
            time.sleep(1)
        print(delayStr,f"."(sec+1))
        # print(' '*WIDTH,end="\r")
        last_str.append(delayStr)
    time.sleep(1)
    return last_str

def show_decision_menu(prompt:str,messageStr:str,last_str:list=[],validChoices:dict={}):
    # to replace
    pass



def reformat_str(message_list:list,additional_sub_width:int=0):
    m_list = []
    if additional_sub_width>= WIDTH:
        raise TypeError
    else:
        text_width = WIDTH-additional_sub_width
    for m in message_list:
        if "\n" in m:
            mn = reformat_str(m.split('\n'))
            m_list.extend(mn)
        elif len(m) >= text_width:
            mn = []
            while len(m) >=text_width:
                n_m = m[:text_width]
                mn.append(n_m)
                m = m[text_width:]
            mn.append(m)
            m_list.extend(mn)
        else:
            m_list.append(m)
    return m_list

def limit_height(last_str:list=[],add_delay:bool=False):
    if add_delay:
        height_limit = HEIGHT-2
    else:
        height_limit=HEIGHT-1

    if len(last_str)> height_limit:
        last_str = last_str[height_limit:]
    elif len(last_str)<height_limit:
        empty_limit = height_limit-len(last_str)
        empty_str = ["" for i in range(empty_limit)]
        last_str = empty_str + last_str
    return last_str
    
def center_text(last_str:list,borderLeft:str="|",borderRight:str="|",blank:str=" "):
    borderLen = len(borderLeft) +len(borderRight)
    if borderLen >= WIDTH:
        raise ValueError
    widthMin = WIDTH - borderLen
    centered_list = []
    for string in last_str:
        if string > WIDTH:
            return center_text(reformat_str(last_str,widthMin))
        strLen = len(string)
        if strLen+borderLen == WIDTH:
            # string is as long as sides
            new_string = f"{borderLeft}{string}{borderRight}"
        elif strLen == 0:
            new_string = f"{borderLeft}{blank*widthMin}{borderRight}"
        else:
            widthRem = widthMin - strLen
            widthLeft = int(widthRem/2)
            widthRight = widthRem - widthLeft
            new_string = f"{borderLeft}{blank*widthLeft}{string}{blank*widthRight}{borderRight}"
        centered_list.append(new_string)
    return centered_list

