import os
import time
from assets.screen_settings import HEIGHT,WIDTH,FRAME_RATE

assert WIDTH != 0
assert HEIGHT != 0

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

def show_decision_menu(prompt:str,menu_list:list=[],last_str:list=[],validChoices:dict={}):
    # to replace
    os.system('cls')
    
    menu_element = center_text([prompt])
    modifiedHeight = HEIGHT - (len(menu_element)+1)
    if len(menu_list) != 0:
        split = 0
        if (len(menu_element)+ len(menu_list))> modifiedHeight:
            # menu_list too long for normal view try to divide by 2?
            split = 2
        if (len(menu_element)+ (len(menu_list)/2)) > modifiedHeight:
            split = 3
        if (len(menu_element)+ (len(menu_list/3)))> modifiedHeight:
            raise TypeError
            # see if can instead do a scroll?
        menu_list = format_menu_list(menu_list,split)


def format_menu_list(menu_list:list=[],split:int=0,borderLeft="|",borderRight="|",blank=" "):
    modified_width = WIDTH - (len(borderLeft) +len(borderRight))
    if split>0:
        col_width = modified_width//split
        new_menu = menu_list.copy()
        split_index = len(new_menu)/split
        col_list = []
        while len(new_menu) > split_index:
            col_list.append(new_menu[:split_index])
            new_menu = new_menu[split_index:]
        if len(new_menu)>0:
            col_list.append(new_menu)
            

    else:
        col_width = modified_width
        col_list = [menu_list.copy()]
    
    last_val = col_list.index(col_list[-1])
    new_col = []
    for ind, col in enumerate(col_list):
        if ind == 0:
            borderLeft = "|"
        else:
            borderLeft = ""
        if ind == last_val:
            borderRight = "|"
        else:
            borderRight = ""
        center_col = center_text(col,borderLeft,borderRight,blank,modified_width=col_width)
        if len(center_col)>HEIGHT:
            raise ValueError
        new_col.append(center_col)
    if len(new_col) == 1:
        # only one column
        return new_col[0]
    else:
        # get by row
        row_str = []
        max_length = max([len(row) for row in new_col])
        for ind in range(max_length):
            row = []
            for ind,list_obj in enumerate(new_col):
                try:
                    list_obj[ind]
                    row.append(list_obj[ind])
                except IndexError:
                    if ind == 0:
                        borderLeft = "|"
                    else:
                        borderLeft = ""
                    if ind == (len(new_col)-1):
                        borderRight = "|"
                    else:
                        borderRight = ""

                    empty_layer = center_text([],borderLeft,borderRight,modified_width=col_width)
                    row.append(empty_layer)
            row_str.append("".join(row))
        return row_str
        
        
            




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
    
def center_text(last_str:list,borderLeft:str="|",borderRight:str="|",blank:str=" ",modified_width:int=None):
    if modified_width == None:
        modified_width = WIDTH

    borderLen = len(borderLeft) +len(borderRight)
    if borderLen >= modified_width:
        raise ValueError
    widthMin = modified_width - borderLen
    centered_list = []
    for string in last_str:
        if string > modified_width:
            return center_text(reformat_str(last_str,widthMin))
        strLen = len(string)
        if strLen+borderLen == modified_width:
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
    if len(last_str) == 0: #making empty
        return f"{borderLeft}{blank*widthMin}{borderRight}"
    return centered_list

def format_borders(last_str:list,header:str=None,header_indent:int=0,hasPrompt:bool=False,prompt_sign:str="> ",corners:set=("+","+","+","+"),walls:set=("|","-","|","-"),blank:str=" "):
    # corner are ul, dl, ur, dr
    # walls are left, up, right, down
    if not isinstance(header,str):
        header_str = add_header(corner_left=corners[0],corner_right=corners[2],wall=walls[1])
    else:
        header_str = add_header(header,header_indent,corner_left=corners[0],corner_right=corners[2],wall=walls[1])
    if hasPrompt:
        end_str = add_base(hasPrompt,prompt=prompt_sign,corner_left=corners[1],corner_right=corners[3],wall=blank)
    else:
        end_str = add_base(False,corner_left=corners[1],corner_right=corners[3],wall=walls[3])

    modified_height = (HEIGHT - len(header_str))-len(end_str)
    if modified_height == 0:
        raise ValueError
    heightModifier = (len(header_str)+len(end_str))
    mid_str = add_mid(last_str,borderLeft=walls[0],borderRight=[2],blank=blank,heightModifier=heightModifier)
    
    new_list = []
    for x in [header_str,mid_str,end_str]:
        if len(x) == 0:
            raise ValueError
        elif len(x) == 1:
            new_list.append(x)
        else:
            new_list.extend(x)
    return new_list
        
def add_mid(last_str:list=[],borderLeft:str="|",borderRight:str="|",blank:str=" ",heightModifier:int=2):
    if len(last_str)>0:
        mid_str = center_text(last_str,borderLeft,borderRight,blank)
    else:
        mid_str = []
    modified_height = (HEIGHT - heightModifier)
    if len(mid_str) > modified_height:
        mid_str = mid_str[-modified_height:] # get end of list? Hopefully correct order
    elif len(mid_str) < modified_height:
        slack = modified_height-len(mid_str)
        mid_gap = WIDTH - (len(borderLeft)+len(borderRight))
        slack_str = [f"{borderLeft}{blank*mid_gap}{borderRight}" for s in range(slack)]
        mid_str = slack_str + mid_str
    # otherwise matches
    return mid_str
        

def add_base(hasPrompt,prompt:str="> ",corner_left="+",corner_right="+",wall=" "):
    if hasPrompt:
        base_str = f"{corner_left}{prompt}"
        cursor_pt = len(base_str)
    else:
        base_str = f"{corner_left}"
        cursor_pt = 0
    wall_gap = WIDTH-len(corner_right)
    base_str = f"{base_str}{wall*wall_gap}{corner_right}"
    if hasPrompt:
        base_str = f"{base_str}\r{base_str[:cursor_pt]}"
    return base_str

def add_header(header_text:str=None,header_indent:int=0,corner_left:str="+",corner_right:str="+",wall:str="-"):
    if header_text == None:
        return f"{corner_left}{wall*(WIDTH-2)}{corner_right}"
    if len(header_text) > WIDTH:
        # header too long
        # header_text = header_text[:(WIDTH//4)]
        raise ValueError
    if header_indent > WIDTH:
        raise ValueError
    if (len(header_text) + header_indent) > WIDTH:
        # header string and indent too long.
        raise ValueError
    if (len(header_text)+ header_indent + (len(corner_right) + len(corner_left))) > WIDTH:
        #header + corners too long
        raise ValueError
    
    # header should fit
    header_str = f"{corner_left}{wall*header_indent}{header_text}"
    if (len(header_str) +len(corner_right)) == WIDTH:
        return f"{header_str}{corner_right}"
    elif (len(header_str) + len(corner_right)) > WIDTH:
        # TOO LONG AGAIN
        raise ValueError
    else:
        remaining_wall = (WIDTH - (len(header_str)+1))
        return f"{header_str}{wall*remaining_wall}{corner_right}"

    
    
    

