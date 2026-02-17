from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
# ZoneInfo()
import time
# current_time = datetime.now().astimezone().astimezone(tz=ZoneInfo.utcoffset())
# print(current_time)
#peri = closest aph = farthest
# dateFormat = '%m-%d-%y_%Z_%H:%M'
dateFormat = '%Y-%m-%d %H:%M %z'
Year = 2000
DateTime_of_Perihelion = '2000-01-03 05:18 +0000'
PeriDistance = 0.9833214 #AU
Relative_to_Mean_Per = 4711 #km
DateTime_of_Aphelion = '2000-07-03 23:49 +0000'
AphDistance = 1.0167411 #AU
Relative_to_Mean_Ap = 4607 #km   
Perihelion_Interval = 364.68
# 2000     Jan 03  05:18             Jul 03  23:49       4607 km     364.68 days
# #Jan 3
Zenith = datetime.strptime(DateTime_of_Perihelion,dateFormat)

#July 2
Nadir = datetime.strptime(DateTime_of_Aphelion,dateFormat)

Midlen = Nadir-Zenith
Midlen_sec = timedelta(seconds=Midlen.total_seconds()/2)
#Apr 2 +90.5 days
Umbra = Zenith

#Oct 2?
Penumbra = Nadir+Midlen_sec

Next_Zenith = Penumbra+Midlen_sec

print(Zenith,Nadir,Umbra,Penumbra,Next_Zenith,sep=f'\n---\n')

Total_length = Next_Zenith-Zenith
print(Total_length)
print(Total_length.total_seconds())
cycle = Total_length
quad_core = Total_length/4
ray = Total_length/32
current = Zenith
ray_zone = 0
ray_list = []
while current < Next_Zenith:
    end_ray = current+ray
    print(f"{ray_zone} - {current} to {end_ray}")
    if ray_zone <8:
        quad = 'DULL'
        horizon = 'SHROUDED'
    elif ray_zone < 16:
        quad = 'GLOOM'
        horizon = 'SHROUDED'
    elif ray_zone < 24:
        quad = 'DIM'
        horizon = 'IGNITED'
    elif ray_zone < 32:
        quad = 'BLOOM'
        horizon = 'IGNITED'



    ray_list.append({
        'name': ray_zone,
        'local_start': current.strftime('%m-%d'),'local_end': ((end_ray-timedelta(days=1)).strftime('%m-%d')),
        'quad': quad,
        'horizon': horizon,
    })
    current = end_ray
    ray_zone+=1

grot = timedelta(days=1)
frac = grot/8
flit = frac/8
splint = flit/4
spec = splint/4

earth_settings = {
    "cycle": Total_length.total_seconds(),
    'quad_length': quad_core.total_seconds(),
    "ray_length": ray.total_seconds(),
    'ray_catalog': ray_list,
    'grot':grot.total_seconds(),
    'frac_length':frac.total_seconds(),
    'flit':flit.total_seconds(),
    'splint':splint.total_seconds(),
    'spec':spec.total_seconds(),
    'rem': 0,
    'solar_system':'ALPHA',
    'name':'Earth'
}

def get_ray_sec(ray_cat:list, difference:float):
    for x in ray_cat:
        ls = timedelta(seconds=x.get('local_start'))
        le = timedelta(seconds=x.get('local_end'))
        if difference >= ls and difference <= le:
            return x
        else:
            pass
    raise TypeError


def get_ray(ray_cat:list,month_day:str):
    mm,dd = month_day.split('-')
    mm = int(mm)
    dd = int(dd)
    for r in ray_cat:
        sm,sd = r['local_start'].split('-')
        sm = int(sm)
        sd = int(sd)
        em,ed = r['local_end'].split('-')
        em = int(em)
        ed = int(ed)

        if mm >= sm and mm <=em:
            if mm > sm or (mm == sm and dd>=sd):
                if mm<em or (mm==em and dd<=ed):
            # if dd >=sd and dd <=ed:
                    return r
        elif r['name'] == 31:
            if mm >=sm and dd>=sd:
                return r
            pass
    raise ValueError
    
def convert_binary(number,places:int=4):
    if number < 1:
        return '0'*places
    else:
        newNum = format(int(number),'b')
        newList = [n for n in newNum]
        while len(newList)<places:
            # newList = [n for n in newNum]
            newList = ['0'] + newList
        newNum = ''.join(newList)
        return newNum
    
def get_calc_time(difference:timedelta, time_unit:timedelta):
        times_into = 0
        if difference < time_unit or int(time_unit.total_seconds()) == 0:
            return times_into, difference
        while difference >= time_unit:
            difference -= time_unit
            times_into += 1
        return times_into, difference   
     
def get_day(ray_dict,date_time:datetime,planet_settings):
    
        
    
    
    current_year = date_time.year
    grot = timedelta(seconds=planet_settings.get('grot'))
    frac = timedelta(seconds=planet_settings.get('frac_length'))
    flit = timedelta(seconds=planet_settings.get('flit'))
    splint = timedelta(seconds=planet_settings.get('splint'))
    spec = timedelta(seconds=planet_settings.get('spec'))
    try:
        start_time = datetime.strptime(f"{ray_dict.get('local_start')}-{current_year}",'%m-%d-%Y')
    except ValueError:
        error = True
        sm, sd = ray_dict.get('local_start').split('-')
        target_year = current_year
        sm = int(sm)
        sd = int(sd)
        
        while error:
            try:
                if sd >1:
                    sd = int(sd)-1
                elif sm > 1:
                    sm = int(sm) -1
                    sd = 31
                else:
                    target_year -=1
                    sm = 12
                    sd = 31
                start_time = datetime.strptime(f"{sm}-{sd}-{target_year}",'%m-%d-%Y')
                error = False
            except ValueError:
                error = True

    difference = date_time-start_time
    print(difference)
    grot_time, difference = get_calc_time(difference,grot)
    grots = convert_binary(grot_time)
    print(difference)
    
    frac_time, difference = get_calc_time(difference, frac)
    fracs = convert_binary(frac_time)
    print(difference)
    flit_time, difference = get_calc_time(difference, flit)
    # flit_time = frac_time/flit
    flits = convert_binary(flit_time)
    print(difference)
    splint_time, difference = get_calc_time(difference,splint)
    splints = convert_binary(splint_time,3)
    print(difference)
    spec_time,difference = get_calc_time(difference,spec)
    specs = convert_binary(spec_time,3)
    if difference.total_seconds() > 0:
        print(difference)
        rem = convert_binary(difference.total_seconds(),2)
    # print(f'{grots}.{fracs}.{flits} {splints}..{specs}.{rem}')
    return grots, fracs, flits, splints, specs, rem

def get_day_sec(ray_dict,difference,planet_settings):
    grot = timedelta(seconds=planet_settings.get('grot'))
    frac = timedelta(seconds=planet_settings.get('frac_length'))
    flit = timedelta(seconds=planet_settings.get('flit'))
    splint = timedelta(seconds=planet_settings.get('splint'))
    spec = timedelta(seconds=planet_settings.get('spec'))
    rem = timedelta(seconds=planet_settings.get('rem',0))
    difference = difference - timedelta(seconds=ray_dict.get('local_start'))

    grot_time, difference = get_calc_time(difference,grot)
    grots = convert_binary(grot_time)

    frac_time,difference = get_calc_time(difference, frac)
    fracs = convert_binary(frac_time)

    flit_time, difference = get_calc_time(difference, flit)
    flits = convert_binary(flit_time)

    splint_time, difference = get_calc_time(difference,splint)
    splints = convert_binary(splint_time,3)

    spec_time, difference = get_calc_time(difference, spec)
    specs = convert_binary(spec_time,3)

    rem_time, difference = get_calc_time(difference,rem)
    rems = convert_binary(rem_time,6)
    
    # return grots,fracs,flits,splints,specs,rems
    return grot_time, frac_time, flit_time,splint_time,spec_time,rem_time


def date_to_GPS(date_time:datetime,planet_settings,solar_system:str='A',planet_name:str='UNKNOWN'):
    # get ray
    ray_list = planet_settings['ray_catalog']
    d_ray = get_ray(ray_list,date_time.strftime('%m-%d'))
    if d_ray == None:
        print('error finding ray')
        return 
    ray_name_binary = convert_binary(d_ray.get('name'),6)
    #get day

    grots, fracs, flits, splints, specs, rem = get_day(d_ray,date_time,planet_settings)
    # for x in [ray_name_binary,grots,fracs,flits,splints,specs]:
    #     print(type(x))
    #     if len(str(x)) <= 4:


    return f"{solar_system}: {planet_name} {date_time.year}C | {ray_name_binary}-{grots} | {fracs}:{flits}_{splints}.{specs}.{rem}"


def secs_to_GPS(total_seconds,planet_settings):
    # get ray
    # ray_list = planet_settings['ray_catalog']
    planet_name = planet_settings.get('name')
    solar_system = planet_settings.get('solar_system')
    cycle_length = timedelta(seconds=planet_settings.get('cycle'))
    # ray_length = planet_settings.get('ray_length')
    ray_cat = planet_settings.get('ray_catalog')
    cycle_count, difference = get_calc_time(total_seconds,cycle_length)
    
    d_ray = get_ray_sec(ray_cat,difference)
    
    if d_ray == None:
        print('error finding ray')
        return 
    ray_name = d_ray.get('name')
    ray_name_binary = convert_binary(d_ray.get('name'),6)

    #get day
    # ray_st = d_ray.get('local_start')


    grot_time, frac_time, flit_time, splint_time, specs_time, rem_time = get_day_sec(d_ray,difference,planet_settings)

    grots = convert_binary(grot_time)
    fracs = convert_binary(frac_time)
    flits = convert_binary(flit_time)
    splints = convert_binary(splint_time,3)
    specs = convert_binary(specs_time,3)
    rem = convert_binary(rem_time,6)
    # for x in [ray_name_binary,grots,fracs,flits,splints,specs]:
    #     print(type(x))
    #     if len(str(x)) <= 4:


    return f"{solar_system}: {planet_name} {cycle_count}C | {ray_name_binary}/{grots} | {fracs}:{flits}_{splints}.{specs}.{rem} >>> | {ray_name}/{grot_time} [{round(ray_name/32,2)}%] | {frac_time}:{flit_time}_{splint_time}.{specs_time}.{rem_time}"


# print(f'grot - {grot}\nfrac - {frac}\nflit - {flit}\nsplint - {splint.total_seconds()}\nspec - {spec.total_seconds()}')

# # print(earth_settings)
# for k, v in earth_settings.items():
#     print(k)
#     if type(v) == list:
#         print(*v,sep='\n')
#     else:
#         print(v)

def planet_setup(planet_name:str,solar_system:str,cycle_length:int,rotation_length:int,override:dict=None):

    output = {
    'name': planet_name,
    "cycle": cycle_length,
    'quad_length': cycle_length/4,
    "ray_length" :cycle_length/32,
    "ray_catalog":get_ray_catalog(cycle_length,cycle_length/32),
    'grot':rotation_length,
    'frac_length':rotation_length//8,
    'flit':rotation_length/8//8,
    'splint':rotation_length/8/8//4,
    'spec':rotation_length/8/8/4//4,
    'rem': 1,
    'solar_system':solar_system
    }
    if override != None:
        ray = override.get('ray_length',32)
        frac = override.get('frac',8)
        flit = override.get('flit',8)
        splints = override.get('splints',4)
        specs = override.get('specs',4)
        
        output['ray_length'] = cycle_length/ray
        output['ray_catalog'] = get_ray_catalog(cycle_length,cycle_length/ray)
        output['frac_length'] = rotation_length//frac
        output['flit'] = rotation_length/frac//flit
        output['splint'] = rotation_length/frac/flit//splints
        output['spec'] = rotation_length/frac/flit/splints//specs
    # quad = cycle_length/4
    # ray_length = cycle_length/32
    # ray_catalog = get_ray_catalog(cycle_length,quad,ray_length)

    # #get time settings
    # frac_length = rotation_length//8
    # flit = rotation_length/8//8
    # splint = rotation_length/8/8//4
    # spec = rotation_length/8/8/4//4
    # rem = 0
    return output

    
def get_ray_catalog(cycle_length,ray_length):
    ray_catalog = []
    ray_zone = 0
    current = 0
    while current < cycle_length:
        end_ray = (current+ray_length)-1
        # print(f"{ray_zone} - {current} to {end_ray}")
        if ray_zone <8:
            quad = 'DULL'
            horizon = 'SHROUDED'
        elif ray_zone < 16:
            quad = 'GLOOM'
            horizon = 'SHROUDED'
        elif ray_zone < 24:
            quad = 'DIM'
            horizon = 'IGNITED'
        elif ray_zone < 32:
            quad = 'BLOOM'
            horizon = 'IGNITED'



        ray_catalog.append({
            'name': ray_zone,
            'local_start': current,'local_end': end_ray,
            'quad': quad,
            'horizon': horizon,
        })
        current = (end_ray +1)
        ray_zone+=1
    return ray_catalog




test_date = date_to_GPS(datetime.now()-timedelta(days=3),earth_settings,planet_name='Earth')

print(test_date)

test_date = date_to_GPS(datetime.now()-timedelta(weeks=15),earth_settings,planet_name='Venus')

print(test_date)

test_date = date_to_GPS(datetime.now(),earth_settings,planet_name='Earth_native')

print(test_date)

test_date = date_to_GPS(datetime.now()-timedelta(hours=-4,weeks=-2,seconds=-25999,minutes=3),earth_settings,planet_name='HUB')

print(test_date)

test_list = [
    ['Central','Alpha',600*300000,19*400],
    ['Gardenia','Alpha',timedelta(days=425).total_seconds(),timedelta(days=19,hours=2).total_seconds()],
    ['Robotussin','Alpha',timedelta(days=1004).total_seconds(),timedelta(days=9,hours=1).total_seconds()]
]
for t in test_list:
# print('cycle in earth days',timedelta(seconds=600*300000).days,'\n grot in earth hours',timedelta(seconds=19*400).seconds/3600
# )
    new_planet = planet_setup(*t)
# new_planet['name'] = 'Alpha'

# print(new_planet,sep='\n')
    for n, k in new_planet.items():
        print(n,end=': ')
        if type(k) == list:
            print('')
            # print(*k,sep='\n')
            pass
        elif type(k) == int or type(k) == float:
            print(k,' (earth days:', round(k/3600/24,3),"earth hours:",round(k/3600,3))
        else:
            print(k)

    current_seconds = datetime.now().astimezone()-Zenith
    # current_seconds = timedelta(seconds=current_seconds)

    cur_sec = secs_to_GPS(current_seconds,new_planet)
    print(cur_sec)

print('CURRENT TIME')
while True:
    earth_actual = planet_setup('Earth','Sol',timedelta(days=Perihelion_Interval).total_seconds(),rotation_length=timedelta(hours=23,minutes=56,seconds=4.09).total_seconds(),override={'ray_length':12,'frac':24,'flit':60,'splints':60,'specs':60})
    current_seconds = datetime.now().astimezone()-Zenith
    cur_sec = secs_to_GPS(current_seconds,earth_actual)
    print(cur_sec,end='\r')
    time.sleep(.2)