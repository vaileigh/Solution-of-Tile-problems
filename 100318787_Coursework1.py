# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 14:18:57 2021

@author: jje20gpa
"""

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
    for pos in move_blank (i ,j , n ):
        i1 , j1 = pos
        grid [ i ][ j ] , grid [ i1 ][ j1 ] = grid [ i1 ][ j1 ] , grid [ i ][ j ]
        yield [ i1 , j1 , grid ]
        grid [ i ][ j ] , grid [ i1 ][ j1 ] = grid [ i1 ][ j1 ] , grid [ i ][ j ]

def is_goal(state):
    goal_state = [[3, 2, 0], [6, 1, 8], [4, 7, 5]]
    if count(state, goal_state) == 9:
        return True  
    

def dfs_rec ( path ):
    if is_goal ( path [ -1]):
        return path
    else :
        for nextState in move ( path [-1]):
            if nextState not in path :
                nextPath = path +[ nextState ]
                solution = dfs_rec ( nextPath )
                if solution != None :
                    return solution
    return None

def count (start_state, goal_state):
    n = 0;
    print(str(start_state))
    '''
    for row in range(len(start_state)):
        for column in range(len(start_state[row])):
            if start_state[row][column] == goal_state[row][column]:
                n += 1
                '''
    return n


def print_state (text, state):
    print(text)
    for i in state[2]:
        print(str(i))

'''
start_state =[]    
start_state.append([0, 0, [[0, 7, 1], [4, 3, 2], [8, 6, 5]]])
goal_state = [0, 2, [[3, 2, 0], [6, 1, 8], [4, 7, 5]]]

print("Count: " + str(count(start_state, goal_state)))

line = []
not_goal = True

while not_goal:
    for ss in start_state:
        for nextState in move ( ss ):
            #print ( nextState )
            line.append(nextState)
        
        count_tiles = []
        
        for l in line:
            count_tiles.append(count(l, goal_state))
        
        lower = []
        for c in range(len(count_tiles)):
            if c == 0:
                lower.append(c)
            else:
                for low in range(len(lower)):
                    if count_tiles[c] < count_tiles[lower[low]]:
                        lower.clear()
                        lower.append(c)
                        break
                    elif count_tiles[c] == count_tiles[lower[low]]:
                        lower.append(c)
        print(str(lower))
        start_state.clear()
        for l in lower:
            start_state.append(line[l])
    not_goal = False
'''
start_state = [0, 0, [[0, 7, 1], [4, 3, 2], [8, 6, 5]]]
path = dfs_rec(start_state)   
#for nextState in move ( start_state ):
    #print ( nextState )

print(path)      
                
    


