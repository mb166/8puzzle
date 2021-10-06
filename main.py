#
#
#

import random
import node
import copy

##### Functions
solved = False

def randomizePuzzle():
    random.shuffle(puzzle)

def printPuzzle():
    for i in range(9):
        print(str(puzzle[i]), end = ' ')
        if(((i+1)%3) == 0):
            print(" ", end='\n')
      

def goalCheck():
    if puzzle == goalState:
        return True
    else:
        return False

def findEmpty(boardState):
    indexCounter = 0
    for current in boardState:
        if current == 0:
            return indexCounter
        else:
            indexCounter += 1

def moveToEmpty(boardState, emptyIndex, toMoveIndex):
    temp = boardState[toMoveIndex]
    boardState[toMoveIndex] = boardState[emptyIndex]
    boardState[emptyIndex] = temp

def getManhattanCost(boardState):
    cost = 0
    indexCounter = 0
    for current in boardState:
        if current == 0:
            indexCounter += 1
            continue
        
        current = current - 1
        gx = current % 3
        gy = current // 3

        x = indexCounter % 3
        y = indexCounter // 3

        tempCost = (abs(x - gx) + abs(y - gy))
        cost += tempCost
        #print((current+1)," ", tempCost)
        indexCounter += 1

    return cost

def nextMove(currentNode):
    if currentNode.state == goalState:
        solved = True
        printSolution(currentNode)
        return

    emptySpace = findEmpty(currentNode.state)
    emptyNeighbors = neighbors[emptySpace]

    for neighbor in emptyNeighbors:
        newBoardState = copy.deepcopy(currentNode.state)
        moveToEmpty(newBoardState, emptySpace, neighbor)
        newNode = node.Node(newBoardState, (currentNode.depth+1), currentNode, (getManhattanCost(newBoardState)))
        if newNode.state == goalState:
            print("Solution: ")
            solved = True

            printSolution(newNode)
            return
        if ((isExplored(newNode.state)) == False):
            unexploredNodes.append(newNode)

def printSolution(solvedNode):
    currentNode = solvedNode
    while(currentNode.parent != None):
        print("Move: ", currentNode.depth)
        currentNode.printThis()
        currentNode = currentNode.parent
    else:
        print("Move: ", currentNode.depth)
        currentNode.printThis()
    quit()

def findNextMove():
    nextNode = None
    nextNodeCost = 10000
    nodeIndexCounter = 0
    nextNodeIndex = 0
    for node in unexploredNodes:
        tempCost = node.cost + node.depth
        if tempCost < nextNodeCost:
            nextNode = node
            nextNodeCost = node.cost + node.depth
            nextNodeIndex = nodeIndexCounter
        nodeIndexCounter += 1
    unexploredNodes.pop(nextNodeIndex)
    exploredNodes.append(nextNode)
    return nextNode

def isExplored(boardState):
    for current in exploredNodes:
        if current.state == boardState:
            return True

    return False

def solvablePuzzle(startingPuzzle):
    inversions = 0
    for i in range(0,9):
        for j in range(i+1, 9):
            if(startingPuzzle[j] != 0 and startingPuzzle[i]!= 0 and startingPuzzle[i] > startingPuzzle[j]):
                inversions += 1
    
    if(inversions % 2 == 0):
        return True
    else:
        return False



#### "Main"
puzzle = [1,2,3,4,5,6,7,8,0]

goalState = [1,2,3,4,5,6,7,8,0]

unexploredNodes = []
exploredNodes = []

#has all adjacent indices
neighbors = {
    0 : [1,3],
    1 : [0,2,4],
    2 : [1,5],
    3 : [4,0,6],
    4 : [3,5,1,7],
    5 : [4,2,8],
    6 : [7,3],
    7 : [6,8,4],
    8 : [7,5],
}
randomizePuzzle()
while solvablePuzzle(puzzle) == False:
    print("puzzle: ", puzzle, " not solvable. generating new puzzle")
    randomizePuzzle()
#puzzle = [1,5,0,3,2,8,4,6,7]
#puzzle = [1,2,3,4,5,6,7,0,8]
startNode = node.Node(puzzle, 0, None, (getManhattanCost(puzzle)))
print("Starting puzzle cost: ", startNode.cost, "Starting puzzle: ")
startNode.printThis()
unexploredNodes.append(startNode)

while(solved == False):
    nextNode = findNextMove()
    nextMove(nextNode)
