# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 18:41:49 2015

@author: pdelboca
"""
#!/usr/bin/python
import numpy as np
def next_move(posr, posc, board):
    rows = np.array([])
    cols = np.array([])
    for idx, row in enumerate(board):
        if 'd' in row:
            rows = np.append(rows, idx)
            cols = np.append(cols, row.index('d'))            
    closer_point = np.argmin(rows + cols)
    
    diff_row = rows[closer_point] - posr # if > 0: dirt is below, else above
    diff_col = cols[closer_point] - posc # if > 0: dirt is RIGHT, else LEFT
    
    if diff_row == 0 and diff_col == 0:
        return "CLEAN"
    
    if diff_row > 0:
        return 'DOWN'
    elif diff_row < 0:
        return 'UP'
    if diff_col > 0:
        return 'RIGHT'
    elif diff_col < 0:
        return 'LEFT'
    

if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(5)]
    print next_move(pos[0], pos[1], board)

