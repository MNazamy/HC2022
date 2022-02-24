class Project:
    rolesRequired = []

    def __init__(self, n, d, s, b, r):
        self.name = n
        self.numberOfDays = d
        self.score = s
        self.bestBefore = b
        self.numRoles = r
    
    def addRole(self,skillName, skillLvl):
        self.rolesRequired.append( (skillName, skillLvl) )

    def debug(self):
        print(f"Project Name: {self.name} - {self.numberOfDays} - {self.score} - {self.bestBefore} - {self.numRoles}")
        for i in self.rolesRequired:
            print(f"   {i[0]} -- {i[1]} ")