#!/bin/python
def nextMove(n,r,c,grid):
    for idx, row in enumerate(grid):
        if 'p' in row:
            princess = (idx, row.index('p'))
    diff_row = princess[0] - r # if > 0: Pricess is below, else above
    diff_col = princess[1] - c # if > 0: Princess is RIGHT, else LEFT
    
    if diff_row > 0:
        return 'DOWN'
    else:
        return 'UP'
    if diff_col > 0:
        return 'RIGHT'
    else:
        return 'LEFT'
    
n = input()
r,c = [int(i) for i in raw_input().strip().split()]
grid = []
for i in xrange(0, n):
    grid.append(raw_input())

print nextMove(n,r,c,grid)