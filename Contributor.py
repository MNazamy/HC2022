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
    
    def upgradeSkill(self,skillName):
        if (self.skills.get(skillName, default=0) > 0):
            self.skills[skillName] = self.skills.get(skillName) + 1
        else:
            self.skills[skillName] = 1 

    def checkSkillLevel(self, skillName):
        if (self.skills.get(skillName, default=0) > 0):
            return self.skills.get(skillName)
        else:
            return 0 
    
