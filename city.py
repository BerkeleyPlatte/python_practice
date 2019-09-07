class City:
    def __init__(self):
        self.name = ""
        self.mayor = ""
        self.year = 0
        self.buildings = ["square one", "round one"]
    
    def __str__(self):
        return self.name
    
    def add_building(self, building):
        self.buildings.append(building)