# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 14:18:57 2021
@author: jje20gpa
"""
from datetime import datetime
import copy
import itertools

def move_blank (i ,j , n ):
    if i +1 < n :
        yield ( i +1 , j )
    if i -1 >= 0:
        yield (i -1 , j )
    if j +1 < n :
        yield (i , j +1)
    if j -1 >= 0:
        yield (i ,j -1)

def move ( state ):
    [i ,j , grid ]= state
    n = len ( grid )
    # print(str(i)+" " + str(j) +" "+ str(n));
    for pos in move_blank (i ,j , n ):
        i1 , j1 = pos
        grid = copy.deepcopy(grid)
        grid [ i ][ j ] , grid [ i1 ][ j1 ] = grid [ i1 ][ j1 ] , grid [ i ][ j ]
        yield [ i1 , j1 , grid ]
        grid [ i ][ j ] , grid [ i1 ][ j1 ] = grid [ i1 ][ j1 ] , grid [ i ][ j ]

def is_goal(path, goal_state):
    if goal_state == path[-1]:
        return True;
    #if count(first, path, goal_state) == 9:
        #return True  
    return False
    

def dfs_rec ( path , goal_state, depth, f):
    if depth == 0:
        return None;
    
    if is_goal (path, goal_state):
        return path
    else :
        for nextState in move (path[-1]):
            newf = depth + h([nextState], goal_state)
            #print(str(newf) + " " + str(f));
            if newf <= f:
                #print(str(newf) + " " + str(f));
                if nextState not in path :
                    nextPath = path + [ nextState ]
                    solution = dfs_rec ( nextPath , goal_state, depth - 1, newf)
                    if solution != None :
                        return solution
    return None

def h (start_state, goal_state):
    n = 0;
    start = start_state[-1]
    start = start[-1]
    goal_state = goal_state[-1]
    
    for row in range(len(start)):
        length = len(start)
        for column in range(length):
            if start[row][column] != goal_state[row][column] and start[row][column] != 0:
                    n += 1
    return n

goal_state = [0 ,2 , [[3, 2, 0], [6, 1, 8], [4, 7, 5]]]
start_state = [0, 0, [[0, 7, 1], [4, 3, 2], [8, 6, 5]]]
depth = 0;


init_time = datetime.now()

for depth in itertools.count():
    f = depth + h([start_state], goal_state)
    path = dfs_rec([start_state], goal_state, depth, f)
    if path != None:
        print(path)
        break; 
fin_time = datetime.now()
print("Execution time (for loop): ", (fin_time-init_time))

        
