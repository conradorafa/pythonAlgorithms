#!/bin/python3

import os
import sys



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
#Slow Solution O(n^2)
    for x in range(0, d):
        t = a[0]
        for i in range(0, n-1): 
            a[i] = a[i+1]
        
        a[n-1] = t
    
    print(" ".join('%01d'%x for x in a))
