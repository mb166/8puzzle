class Node:
    def __init__(self, state, depth, parent, cost):
        self.state = state
        self.depth = depth
        self.parent = parent
        self.cost = cost

##prints the state of the game board
    def printThis(self):
        for i in range(9):
            print(str(self.state[i]), end = ' ')
            if(((i+1)%3) == 0):
                print(" ", end='\n')
        print("-----------")