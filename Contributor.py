class Contributor:
    def __init__(self, contributorName, numberOfSkills):
        self.name = contributorName
        self.numSkills = numberOfSkills
        self.onProject = False
        self.skills = {}
    
    def addSkill(self, skillName, skillLvl):
        self.skills[skillName] = skillLvl
    
    def isOnProject(self):
        return self.onProject
    
    def assignToProject(self):
        self.onProject = True
    
    def completeProject(self):
        self.onProject = False
    
    def upgradeSkill(self):
        pass

    def hasSkill(self):
        pass
    
    def debug(self):
        print(f"My name is {self.name} and I'm good at: ")
        for i in self.skills.keys():
            print(f"      {i} -- {self.skills[i]} ")