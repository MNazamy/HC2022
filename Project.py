class Project:
    def __init__(self, n, d, s, b, r):
        self.name = n
        self.numberOfDays = d
        self.score = s
        self.bestBefore = b
        self.numRoles = r
        self.rolesRequired = []
    
    def addRole(self,skillName, skillLvl):
        self.rolesRequired.append( (skillName, skillLvl) )

    def sortingValue(self, currentDay):
        bestByOverage = self.bestBefore - currentDay - self.numberOfDays
        if bestByOverage >= 0: bestByOverage = 0
        return (self.score - bestByOverage) / self.numberOfDays


    def debug(self):
        print(f"Project Name: {self.name} - {self.numberOfDays} - {self.score} - {self.bestBefore} - {self.numRoles}")
        for i in self.rolesRequired:
            print(f"   {i[0]} -- {i[1]} ")