class Planet():
    def __init__(self,navLoc,name,description,economy=None,products=None,population=None,fluidCapital=None):
        self.navLoc:int = navLoc
        self.nameL:str = name
        self.description:str = description
        self.economy:int = economy
        self.products:list = products
        self.population:int = population
        self.fluidCapital:int = fluidCapital
        self.planetRelations:dict = {}
        # self.likes:dict = needs
        # self.hates:dict = hates
        self.playerImpact:int = 0

        # if self.economy == None:
    def __str__(self):
        return f"{self.name}: {self.description}\n{self.products}"
