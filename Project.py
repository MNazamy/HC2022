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

    def startProject(self, currDay, cl):
        self.contributorList = cl
        for contributor in self.contributorList:
            contributor.assignToProject()

        self.finishDay = currDay + self.numberOfDays
        return self.finishDay


    def finishProject(self, currDay):
        for i in range(self.numRoles):
            if self.contributorList[i].checkSkillLevel() <= self.rolesRequired[i][1]:
                self.contributorList[i].upgradeSkill()

            if currDay <= self.bestBefore:
                return self.score
            elif currDay-self.bestBefore < self.score:
                return self.score-(currDay-self.bestBefore)
            else:
                return 0
        


