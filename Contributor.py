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
        try:
            self.skills[skillName] += 1
        except:
            self.skills[skillName] = 1


    def checkSkillLevel(self, skillName):
        try:
                return self.skills[skillName]
        except:
            return 0
    
