
from datetime import datetime
import copy
start_state = [1,0,[[1,2,3],[0,4,6],[7,5,8]]]
goal_state = [2,2,[[1,2,3],[4,5,6],[7,8,0]]]

""" Generate a Node class """
class Node:
    """ Initialise the node with data, level of the node, the fvalue = start level + h and parent """
    def __init__(self,data,level,fval,parent):
        self.data = data
        self.level = level
        self.fval = fval
        self.parent = parent
    
    """ Move to blank space with UP or DOWN or RIGHT or LEFT """
    def move_blank (i ,j , n ):
        if i +1 < n :
            yield ( i +1 , j )
        if i -1 >= 0:
            yield (i -1 , j )
        if j +1 < n :
            yield (i , j +1)
        if j -1 >= 0:
            yield (i ,j -1)
        
    """ Get the possible state using a generator function"""
    def move (self, state ):
        [i ,j , grid ] = state
        n = len ( grid )
        
        # print(str(i)+" " + str(j) +" "+ str(n));
        for pos in Node.move_blank (i ,j , n ):
            i1 , j1 = pos
            """ Copy the grid without effect the original object """
            newgrid = copy.deepcopy(grid)
            newgrid [ i ][ j ] , newgrid [ i1 ][ j1 ] = grid [ i1 ][ j1 ] , grid [ i ][ j ]
            yield [ i1 , j1 , newgrid ]
            newgrid [ i ][ j ] , newgrid [ i1 ][ j1 ] = grid [ i1 ][ j1 ] , grid [ i ][ j ]
    
    """ Generate child nodes from the parent state and return all the children"""
    def generate_child(self):
        self.children = []
        """ Loop every possible movement on current state """
        for nextState in self.move (self.data):
            child_node = Node(nextState,self.level+1,0, self.data)
            self.children.append(child_node)
        return self.children

""" Generate a Tiles class """
class Tiles:
    """ Initialize the tiles size by the specified size,open and closed lists to empty """
    def __init__(self,size):
        self.n = size
        self.open = []
        self.closed = []


    """ Create a function to return f value = h + start level """
    def f(self,start,goal):
        return self.h(start.data,goal)+start.level

    """ Create a function to return h value """
    def h(self,start,goal):
        start = start[-1]
        goal = goal[-1]
        count = 0
        
        """ Calculate the different between goal and current state but 0 not count"""
        for i in range(0,self.n):
            for j in range(0,self.n):
                if start[i][j] != goal[i][j] and start[i][j] != 0:
                        count += 1
        return count
        
    """ main function to run """
    def process(self):        
        """ start, goal with no same f value"""
        #start = [1,1, [[2,8,3],[1,0,4],[7,6,5]]]
        #goal = [1,1,[[1,2,3],[8,0,4],[7,6,5]]]
        """ start, goal with 2 same f values """
        #start = [1,0, [[1,2,3],[0,4,6],[7,5,8]]]
        #goal = [2,2, [[1,2,3],[4,5,6],[7,8,0]]]
        """ start, goal with complex tree """
        start = [0,0,[[0, 7, 1], [4, 3, 2], [8, 6, 5]]]
        goal = [0,2,[[3, 2, 0], [6, 1, 8], [4, 7, 5]]]
        
        """ Add start to node"""
        start = Node(start,0,0,start)
        """ Calculate the f value """
        start.fval = self.f(start,goal)
        """ Put the start node in the open list"""
        self.open.append(start)
        won = False
        while not won:
            curr = self.open[0]
            """ Apply an infinite loop """
            while True:
                """ The current node is open[0] because the list table are sorted with f value """
                cur = self.open[0]
                """ Looking for same f value state """
                if cur.fval == curr.fval:
                    
                    """ If is goal print all the steps """
                    if(self.h(cur.data,goal) == 0):
                        s = self.closed[len(self.closed) - 1]
                        path = []
                        path.append(cur)
                        path.append(s)
                        while True:
                            if path[len(path)-1].parent == self.closed[0]:
                                path.append(path[len(path)-1].parent)
                                break
                            path.append(path[len(path)-1].parent)
                        for i in reversed(range(len(path))):
                            print(str(path[i].data))
                        won = True
                        break
                    """ Generate children from the current state """
                    for i in cur.generate_child():
                        """ Calculate the f value """
                        i.fval = self.f(i,goal)
                        """ Initialise the parent """
                        i.parent = cur
                        """ Store all the children into open list """
                        self.open.append(i)
                    """ Store the lower f value current state into closed list """
                    self.closed.append(cur)
                    """ Delete the first item in open list """
                    del self.open[0]
                    """ Sort the open list with f value in ascending order """
                    self.open.sort(key = lambda x:x.fval,reverse=False)
                else:
                    break



""" Main function """
def main():
    """ begin time """
    begin = datetime.now()
    til = Tiles(3)
    til.process()
    """ End time """
    end = datetime.now()
    """ Print Program execution time """
    print("Execution time: ", (end-begin))

""" Ask the program to run main function """
if __name__ == "__main__":
    main()
