class Player():
    def __init__(self,loc,points,title,cargoManifest,shipStats):
        self.loc = loc
        self.points = points
        self.title = title
        self.cargoManifest = cargoManifest 
        self.message = ''
        #letters: [(#, destination,item)], packages: [(#,destination,item)]
        self.shipStats = shipStats #cargoSpaceRemaining, speed, fuel, durability 
    def all_status(self):
        #still busted and dont know why
        baseStats = f"{self.loc.nameL}\n{self.points} Units\n{self.cargo()}\n{self.status}"
        # if self.shipStats.get('fuelRemaining')\
        print(baseStats)
        fuel_perc = self.check_fuel()
        print(f"Fuel: {fuel_perc}")
        return f"{baseStats}\n{fuel_perc}\n\n"
    def __str__(self):
        baseStats = f"{self.loc.nameL}\n{self.points} Units\n{self.cargo()}\n{self.status}"
        # if self.shipStats.get('fuelRemaining')\
        fuel_perc = self.check_fuel()
        return f"{baseStats}\n{fuel_perc}\n\n"
    
    def cargo(self):
        cargoStr = ""
        for key, value in self.cargoManifest.items():
            cargoStr += f"\n{key}:"
            try:
                for entry in value:
                    quantity,destination,item, origin = entry
                    cargoStr += f"\n{quantity} {item} to {destination.nameL} from {origin.nameL}"
            except IndexError:
                cargoStr += ""
        return cargoStr
    
    def status(self):
        statusStr = f"\n\nShip Stats:\n"
        for key, value in self.shipStats.items():
            statusStr += f"{key}: {value}\n"
        return statusStr
    
    def check_fuel(self,showWarning:bool=True):
        fuelMax = self.shipStats.get('fuelSpace')
        fuelRem = self.shipStats.get('fuelRemaining')
        fuelPerc = round(fuelRem/fuelMax,2)
        if fuelPerc <= .25:
            print(f'LOW FUEL: {fuelPerc*100}%')
        return fuelPerc

    def ship_cargo_set(self):
        # print(self.shipStats.keys())
        cargoMax = self.shipStats.get('cargoSpace')
        cargoFill = 0
        for k,v_list in self.cargoManifest.items():
            for v in v_list:
                cargoFill += v[0]
        cargoRem = cargoMax - cargoFill
        self.shipStats['cargoSpaceRemaining'] = cargoRem
        return
    
    def ship_fuel_drain(self,drainAmount)-> bool:
        # fuelMax = self.shipStats.get('fuelSpace')
        fuelRem = self.shipStats.get('fuelRemaining')
        if fuelRem == 0:
            print('Not enough fuel to launch!')
            return False
        if drainAmount > fuelRem:
            print('Not enough fuel to reach destination!')
            return False
        fuelRem -= drainAmount
        self.shipStats['fuelRemaining'] = fuelRem
        return True

    def ship_refuel(self)->bool:
        fuelMax = self.shipStats.get('fuelSpace')
        fuelRem = self.shipStats.get('fuelRemaining')

        if fuelRem == fuelMax:
            print('Fuel tank already at maximum')
            return False
        self.shipStats['fuelRemaining'] = fuelMax
        return True
    

