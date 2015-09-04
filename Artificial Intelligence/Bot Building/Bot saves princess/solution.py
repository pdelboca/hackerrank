#!/bin/python
def displayPathtoPrincess(m,grid):
    #grid -> ['---', '-m-', 'p--']    
    for idx, row in enumerate(grid):
        if 'p' in row:
            princess = (idx, row.index('p'))
        if 'm' in row:
            bot = (idx, row.index('m'))
    diff_row = princess[0] - bot[0] # if > 0: Pricess is below, else above
    diff_col = princess[1] - bot[1] # if > 0: Princess is RIGHT, else LEFT

    path = ""    
    if diff_row > 0:
        path = path + 'DOWN\n' * diff_row
    else:
        path = path + 'UP\n' * abs(diff_row)
    if diff_col > 0:
        path = path + 'RIGHT\n' * diff_col
    else:
        path = path + 'LEFT\n' * abs(diff_col)
    print path

    
m = input()

grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())

displayPathtoPrincess(m,grid)