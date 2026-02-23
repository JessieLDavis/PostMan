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
        print(f'[{userResponse} selected]\n')
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

def prompt_response(valid_options:dict={'search':'Find letters at the Post Office or packages at different planets','deliver':'Drop letters or packages at the target destination','leave':'Travel to another station or planet','help':'Show choice options','quit':'Exit the game'}):
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


    