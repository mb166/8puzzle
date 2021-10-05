#
#
#

import random

##### Functions
def randomizePuzzle():
    listOfNumbers = [1,2,3,4,5,6,7,8,0]
    random.shuffle(listOfNumbers)
    listCounter = 0
    for i in range(3):
        for x in range(3):
            puzzle[i][x] = listOfNumbers[listCounter]
            listCounter += 1

def printPuzzle():
    for i in range(3):
        for x in range(3):
            print(str(puzzle[i][x]), end = ' ')
        else:
            print(' ', end = '\n')   

def goalCheck():
    if puzzle == goalState:
        return True
    else:
        return False

#### "Main"
puzzle = [[1,2,3],
          [4,5,6],
          [7,8,0]]

goalState = [[1,2,3],
            [4,5,6],
            [7,8,0]]

print(goalCheck())

randomizePuzzle()

printPuzzle()
print(goalCheck())