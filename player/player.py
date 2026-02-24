class Player():
    def __init__(self,loc,points,title,cargoManifest,shipStats):
        self.loc = loc
        self.points = points
        self.title = title
        self.cargoManifest = cargoManifest #letters: [(#, destination,item)], packages: [(#,destination,item)]
        self.shipStats = shipStats #cargoSpaceRemaining, speed, fuel, durability 
    def __str__(self):
        return f"{self.loc}\n{self.points}\n{self.cargo()}\n{self.status}"
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
        statusStr = ""
        for key, value in self.shipStats.items():
            statusStr += f"{key}: {value}\n"
        return statusStr
    

            
