
from Contributor import Contributor
from Project import Project
import heapq

def readInput(filename):
    
    with open(filename, "r") as inFile:

        firstLine = inFile.readline()
        words = firstLine.split()
        numContributors = int(words[0])
        numProjects = int(words[1])
        contributors = []
        projects = []

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
                temp.debug()
            
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
                temp.debug()

            projects.append(temp)





def run(fileName):
    # str (skill) -> int (skill level) -> list of people
    skillDict = {}

    # list of all people available for work
    peopleAvailable = []

    #priority queue of projects
    projectPQ = []


    readInput(fileName)


    

        



if __name__ == "__main__":
        run("./a_an_example.in.txt")