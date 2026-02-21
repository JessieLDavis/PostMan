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

        self.inventory = {}

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
        
    def add_inv(self):
        pass
        