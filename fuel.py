#import fuel cost from planet

def fuel_cost(origin,dest):
    pass
    
def refuel_cost(ship,local_price,final_fuel_level:float=1.0,local_tax:float=0.0)->int:
    """Always round up. maybe class function?"""
    current_level = ship.fuel
    max_cap = ship.fuel_cap
    if ship.fuel == ship.fuel_cap:
        return 0
    perc_full = round(current_level/max_cap,3)
    if perc_full <= final_fuel_level:
        return 0
    fuel_final = round(max_cap*final_fuel_level,3)
    fuel_diff = fuel_final-current_level
    #switch to round up?
    price = round((fuel_diff*local_price) + (fuel_diff*local_tax),0)
    return price
    
def refuel(ship,location):
    pass
    