from random import choice


class PostalShip:
    ship_types = ["Tri","Cargo","Discus","Yaught","Nautilus","Wurst"]
    ship_types_dict = {
        "Tri": {
            "fuel_range": [50,100],
            "cost_range":[100,500],
            "inv_range":[100,200],
            "burn_rate":[30,100]
        },
        "Cargo": {
            "fuel_range": [300,500],
            "cost_range":[1000,3000],
            "inv_range":[300,500],
            "burn_rate":[50,80]
        },
        "Discus": {
            "fuel_range": [200,400],
            "cost_range":[300,800],
            "inv_range":[40,80],
            "burn_rate":[30,80]
        },
        "Yaught": {
            "fuel_range": [100,500],
            "cost_range":[1000,5000],
            "inv_range":[200,400],
            "burn_rate":[10,50]
        },
        "Nautilus": {
            "fuel_range": [50,100],
            "cost_range":[50000,80000],
            "inv_range":[1000,2000],
            "burn_rate":[100,300]
        },
        "Wurst": {
            "fuel_range": [50,100],
            "cost_range":[100,500],
            "inv_range":[100,200],
            "burn_rate":[3,9]
        }
    }

    def __init__(self,model_type,quality,official:bool=True):
        if model_type not in PostalShip.ship_types:
            raise TypeError
        ship_ranges = PostalShip.ship_types_dict.get(model_type)
        self.official = self.randomize_values(ship_ranges,quality)

        self.fuel_max = self.official.get('fuel')
        self.fuel_current:int = self.official.get('fuel')
        self.cost = self.official.get('cost')
        self.inv_max = self.official.get('inv')
        self.inv_current = 0
        self.burn_rate = self.official.get('burn')
        self.launch_rate = self.official.get('launch')
        self.name_official = self.ship_name_gen(model_type)
        self.inventory = {}
        self.purchased = False

    def __str__(self):
        if self.purchased:
            return f"Name: {self.name_official}\nFuel: {self.fuel_current}/{self.fuel_max} [{round((self.fuel_current/self.fuel_max)*100,1)}%]\nInventory: {self.get_inventory_counts()}\nResale price: {self.cost} units"
        else:
            return f"Model: {self.name_official}\nMax Fuel: {self.fuel_max}c\nBurn Rate: {self.launch_rate} c/k [{self.burn_rate} c/p] \nMax Inventory: {self.inv_max}\nSell price: {self.cost} units"

    def get_inventory_counts(self):
        inventory_report = []
        for k, v in self.inventory.items():
            full_count = [o.quantity for o in v]
            if len(full_count) == 0:
                full_count = 0
            else:
                full_count = sum(full_count)
            new = f"{k}: {full_count}"
            inventory_report.append(new)
        return ' | '.join(inventory_report)

        

    def randomize_values(self,ship_ranges,quality:float=1.0):
        out_dict = {}
        for k, v in ship_ranges.items():
            new_key = k.split("_")[0]
            new_v = choice(range(*v,step=5))[0]
            new_v = int(new_v*quality)
            if new_v < v[0]:
                new_v = v[0]
            out_dict[new_key] = new_v
        return out_dict
        
    def add_inv(self,object_pending):
        message = None
        if self.inv_current == self.inv_max:
            #no room in the hold
            message = 'Inventory full.'
            # return False, message
        elif (self.inv_current + object_pending.quantity) > self.inv_max:
            message = 'Not enough room in inventory.'

        if isinstance(message,str):
            return False, message
            
        #if no error
        try:
            self.inventory[object_pending.obj_type]
        except KeyError:
            self.inventory[object_pending.obj_type] = []
        self.inventory[object_pending.obj_type].append(object_pending)
    
    