
from Contributor import Contributor
from Project import Project
import heapq

def readInput(filename):
    contributors = []
    projects = []
    skd = {}

    
    with open(filename, "r") as inFile:

        firstLine = inFile.readline()
        words = firstLine.split()
        numContributors = int(words[0])
        numProjects = int(words[1])
        
        #Loop for contributors input
        for _ in range(numContributors):
            line = inFile.readline()
            words = line.split()
            name = words[0]
            numSkills = int(words[1])
            temp = Contributor(name, numSkills)

            # Read in Skills for each contributor
            for __ in range(numSkills):
                line = inFile.readline()
                words = line.split()
                nameOfSkill = words[0]
                skillLvl = int(words[1])
                temp.addSkill(nameOfSkill, skillLvl)

                #creating skill dicitonary
                try:
                    currSk = skd[nameOfSkill]
                except:
                    skd[nameOfSkill] = {}
                    currSk = skd[nameOfSkill]
                try:
                    currSk[skillLvl].append(temp)
                except:
                    currSk[skillLvl] = [temp]
            
            #creating available person list
            contributors.append(temp)



        #Loop for project input
        for _ in range(numProjects):
            line = inFile.readline()
            words = line.split()
            projectName = words[0]
            numDays = int(words[1])
            score = int(words[2])
            bestBefore = int(words[3])
            roles = int(words[4])
            temp = Project(projectName, numDays, score, bestBefore, roles)

                # Read in skills required for each project
            for __ in range(roles):
                line = inFile.readline()
                words = line.split()
                skillNeeded = words[0]
                requiredLvl = int(words[1])
                temp.addRole(skillNeeded, requiredLvl)

            projects.append([temp.sortingValue(0) ,temp])
    return contributors, projects, skd

    

def output(filename, pcount, plist):
    with open(filename, "w") as file:
        file.write(pcount)
        for _ in plist:
            file.write(_.name)
            s = ""
            for person in _.contributorList:
                s += person.name + " "
            file.write(s)



def run(fileName):
    # str (skill) -> int (skill level) -> list of people
    skillDict = {}

    # list of all people available for work
    peopleAvailable = []

    #priority queue of projects
    projectPQ = []

    #list holding project for later execution
    laterList = []

    #priority queue for current projects
    currPrjPQ = []

    score = 0

    projectOrder = []


    peopleAvailable, projectPQ, skillDict = readInput(fileName)

    heapq.heapify(projectPQ)

    day = 0
    projectCount = 0
    projectsWorthPointsAreAvailable = True
    numPeopleAvail = len(peopleAvailable)

    while projectsWorthPointsAreAvailable:
        for _ in projectPQ:
            _[0] = _[1].sortingValue(day)

        heapq.heapify(projectPQ)

        projectAssigned = -1
        while(len(projectPQ) > 0 and numPeopleAvail > 0 and projectPQ[0][0] > 0):
            currPrj = heapq.heappop(projectPQ)
            projectAssigned, numPeopleAvail = checkProject(currPrj[1], peopleAvailable, skillDict, numPeopleAvail)
            if projectAssigned == -1:
                laterList.append(currPrj)
            else:
                currPrjPQ.append([currPrj.numberOfDays-1, currPrj[1]])
                projectOrder.append(currPrj[1])
        
        projectPQ += laterList
        heapq.heapify(projectPQ)
        heapq.heapify(currPrjPQ)

        while(currPrjPQ[0][0] == day):
            currPrj = heapq.heappop(currPrjPQ)[1]
            score += currPrj.finishProject(day)
            projectCount += 1
        
        projectsWorthPointsAreAvailable = projectPQ[0][0] > 0

        day += 1

    output("output.txt", projectCount, projectOrder)


    

        



if __name__ == "__main__":
        run("./a_an_example.in.txt")