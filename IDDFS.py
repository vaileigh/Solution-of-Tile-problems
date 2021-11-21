# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 16:19:06 2021

@author: jje20gpa
"""
from datetime import datetime
import copy
import itertools


start_state = [0, 0, [[0, 7, 1], [4, 3, 2], [8, 6, 5]]]
goal_state = [0 ,2 , [[3, 2, 0], [6, 1, 8], [4, 7, 5]]]

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
def move ( state ):
    [i ,j , grid ]= state
    n = len ( grid )
    # print(str(i)+" " + str(j) +" "+ str(n));
    for pos in move_blank (i ,j , n ):
        i1 , j1 = pos
        """ Copy the grid with effect the original object """
        grid = copy.deepcopy(grid)
        grid [ i ][ j ] , grid [ i1 ][ j1 ] = grid [ i1 ][ j1 ] , grid [ i ][ j ]
        yield [ i1 , j1 , grid ]
        grid [ i ][ j ] , grid [ i1 ][ j1 ] = grid [ i1 ][ j1 ] , grid [ i ][ j ]

""" If the goal state same as the path """
def is_goal(path):
    if goal_state == path[-1]:
        return True;
    return False
    
""" DFS recursion function """
def dfs_rec ( path , depth):
    
    """ The recursion will minus one everytime, if no solution will until depth == 0 return None """
    if depth == 0:
        return None;
    
    """ Check if the path is goal state """
    if is_goal (path ):
        """ The path won't be None when return """
        return path
    else :
        """ Loop every possible movement on current state """
        for nextState in move (path[-1]):
            """ Check if the new state are not in the appear before """
            if nextState not in path :
                nextPath = path + [ nextState ]
                solution = dfs_rec ( nextPath , depth - 1)
                if solution != None :
                    return solution
    return None

""" Main function """
def main():
    """ begin time """
    begin = datetime.now()
    depth = 0;
    
    """ itertool.count() will assign the value 1 , 2, 3 .... n """
    for depth in itertools.count():
        """ Return the path from dfs_rec() function """
        path = dfs_rec([start_state], depth)
        """ if path not = None == solution found """
        if path != None:
            """ Print the solution """
            for p in path:
                print(str(p))
            """ Break when solution has been found """
            break; 
    """ End time """
    end = datetime.now()
    """ Print Program execution time """
    print("Execution time: ", (end-begin))

""" Ask the program to run main function """
if __name__ == "__main__":
    main()
