

def run(filename):
    
    with open(filename, "r") as inFile:

        firstLine = inFile.readline()
        secondLine = inFile.readline()

        print(firstLine )
        print(secondLine)
    
    with open("output.txt","w") as outFile:
        outFile.write("hey")
        

        



if __name__ == "__main__":
        run("input.txt")