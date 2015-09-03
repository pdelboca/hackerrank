# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 09:29:17 2015

@author: pdelboca
"""

import sys
import numpy as np


def load_data():
    # Just Read first line
    arr = sys.stdin.readline().strip().split(" ")
    # Now read all the table    
    data = np.genfromtxt(sys.stdin, dtype=int)
    return data
    
def main():
    # (Mathematics, Physics and Chemistry)
    data = load_data()
    #Correlation coefficient between Mathematics and Physics scores.
    cor1 = np.corrcoef(data[:,0], data[:,1])[0,1]
    sys.stdout.write(str(round(cor1, 2)) + '\n')    
    #Correlation coefficient between Physics and Chemistry scores. 
    cor2 = np.corrcoef(data[:,1], data[:,2])[0,1]
    sys.stdout.write(str(round(cor2, 2)) + '\n')    
    #Correlation coefficient between Chemistry and Mathematics scores.
    cor3 = np.corrcoef(data[:,2], data[:,0])[0,1]
    sys.stdout.write(str(round(cor3, 2)) + '\n')    
    
if __name__ == "__main__":
    main()