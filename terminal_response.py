from random import choices

PLAYER_OPTS = {
'search':'Find letters at the Post Office or packages at different planets',
'deliver':'Drop letters or packages at the target destination',

'check fuel': 'Get current fuel level',
'refuel': 'Get fuel at current market rate',

'leave':'Travel to another station or planet',
'map': 'Show planetary map',
'status': 'Show player stats',
'influence': 'Show player - planet relationship',

'help':'Show choice options',
'quit':'Exit the game'
}
HIDDEN_OPTS = {'listen':{'allOpts':['listen','evesdrop','check diplomacy','planet relationships','planetary relations']}}

def get_menu_response(question:str,option_list:list,title_str:str=None,subtitle_str:str=None,sort_opts:bool=False,addOther:bool=True,other_text:str='Quit'):
    if sort_opts:
        option_list.sort()
    if title_str != None:
        print()
        print('---'*10,title_str,'---'*10)
    if subtitle_str != None:
        base_gap = 10
        if title_str != None:
            base_gap = int((len(title_str)+60)/2)
            if len(subtitle_str)//2==0:
                subtitle_gap = int((len(subtitle_str)+6)/2)
            else:
                subtitle_gap = int((len(subtitle_str)+7)/2)
            base_gap = base_gap-subtitle_gap



        print(' '*base_gap,'** ',subtitle_str,' **')
    # print()
    option_str = [f"{ind+1} - {o}" for ind, o in enumerate(option_list)]
    
    if addOther:
        option_str.append(f"0 - {other_text}")
    option_str = '\n'.join(option_str)

    userResponse = input(f'{question}\n{option_str}\n> ')
    try:
        userResponse = int(userResponse)
        if userResponse == 0 and addOther == True:
            #other allowed
            return other_text
        elif userResponse == 0 and addOther == False:
            raise IndexError
        selected = option_list[userResponse-1]
        print(f'[{userResponse}: {selected} selected]\n')
        return selected
    except ValueError:
        print(f'{userResponse} not accepted. Please only include integers.')
    except IndexError:
        print(f'{userResponse} is not accepted. Please select a value from the list.')
    return get_menu_response(question,option_list,title_str,subtitle_str,sort_opts,addOther,other_text)
    
def get_multiple_choice(question:str,option_list:list,sort_opts:bool=False,add_other:bool=False,other_text:str='Other'):
    if sort_opts:
        option_list.sort()
    option_str = [f"{ind+1} - {o}" for ind, o in enumerate(option_list)]
    
    if add_other:
        option_str.append(f"\n0 - {other_text}")
    option_str = '\n'.join(option_str)
    userResponse = input(f'{question}\n{option_str}\n>')
    try:
        userResponse = int(userResponse)
        if userResponse == 0 and add_other == True:
            #other allowed
            return other_text
        elif userResponse == 0 and add_other == False:
            raise IndexError
        selected = option_list[userResponse-1]
        print(f'[{userResponse} selected]\n')
        return selected
    except ValueError:
        print(f'{userResponse} not accepted. Please only include integers.')
    except IndexError:
        print(f'{userResponse} is not accepted. Please select a value from the list.')
    return get_multiple_choice(question,option_list,sort_opts,add_other,other_text)

def prompt_response(valid_options:dict=PLAYER_OPTS):
    userResponse=input('> ').lower()
    if userResponse == 'help':
        for k, v in valid_options.items():
            print(f'{k} - {v}')
        return prompt_response()
    try:
        valid_options[userResponse]
        return userResponse
    except KeyError:
        print(f'{userResponse} not accepted.')
    return prompt_response()

def get_planet_choice(question:str,playerObj,planetObj):
    # from nav_page import Planet
    includeGas = choices([True,False],[1,4],k=1)[0]
    if playerObj.loc.space_location in ['static','mystery']:
        planet_list = planetObj.get_planets(includeGas=includeGas,onlyNames=False)
    elif playerObj.loc.space_location in ['west','east']:
        planet_list = planetObj.get_planets(includeGas=includeGas,onlyNames=False,side=playerObj.loc.space_location)
    
    option_str = [o.showLoc() for o in planet_list]
    
    # if add_other:
    #     option_str.append(f"\n0 - {other_text}")
    option_str = '\n'.join(option_str)
    userResponse = input(f'{question}\n{option_str}\n>')
    try:
        userResponse = int(userResponse)
        selected = [plan for plan in planet_list if plan.navLoc == userResponse][0]
        print(f'[{selected.nameL} selected]\n')
        return selected
    except ValueError:
        print(f'{userResponse} not accepted. Please only include integers.')
    except IndexError:
        print(f'{userResponse} is not accepted. Please select a value from the list.')
    return get_planet_choice(question,playerObj,planetObj)

def get_binary_response(question:str,optionKeys:list=["y",'n','na'],allowNull:bool=False):
    if len(optionKeys)!=3:
        raise ValueError
    opt_str = ['Yes','No','Null']
    opt_new = []
    if allowNull == False:
        optionKeys.pop()
    for ind, key in enumerate(optionKeys):
        opt_new.append(f"{key} = {opt_str[ind]}")
    opt_new = '\n'.join(opt_new)
    response = input(f'{question}\n{opt_new}\n>') 
    response = response.lower()
    if response not in optionKeys:
        print(f"{response} not accepted.")
        return get_binary_response(question,optionKeys,allowNull)
    actual = opt_str[optionKeys.index(response)]
    if actual == 'Yes':
        return True
    elif actual == 'No':
        return False
    elif allowNull == False:
        print('Error finding response')
        return get_binary_response(question,optionKeys,allowNull)
    else:
        return None