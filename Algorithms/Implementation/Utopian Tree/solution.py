# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 18:06:25 2015

@author: pdelboca
Problem Statement

The Utopian Tree goes through 2 cycles of growth every year. 
The first growth cycle occurs during the spring, when it doubles in height. 
The second growth cycle occurs during the summer, when its height increases by 1 meter.

Now, a new Utopian Tree sapling is planted at the onset of spring. 
Its height is 1 meter. 
Can you find the height of the tree after N growth cycles?
"""
import sys

def calculate_height(cycles):
    height = 1    
    # Itero por todos los ciclos:
    # Si es impar: +1
    # Si es par: *2
    for i in range(cycles):
        if (i % 2) == 1:
            height = height + 1
        else:
            height = 2 * height
    return height
    
def main():
    T = int(sys.stdin.readline().strip())
    for i in range(T):
        cycles = int(sys.stdin.readline().strip())
        print calculate_height(cycles)
    
if __name__ == "__main__":
    main()