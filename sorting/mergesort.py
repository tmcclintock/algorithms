"""
My implementation of mergesort.
"""
import numpy as np

def merge(array):
    N = len(array)
    if N <= 1: return array
    
    left = array[:N/2]
    right = array[N/2:]
    left = merge(left)
    right = merge(right)
    return merge_lists(left,right)

def merge_lists(ar1, ar2):
    new = []
    while ar1 and ar2: #While both are non-empty
        if ar1[0] <= ar2[0]:
            new.append(ar1[0])
            del ar1[0]
        else:
            new.append(ar2[0])
            del ar2[0]
    while ar1:
        new.append(ar1[0])
        del ar1[0]
    while ar2:
        new.append(ar2[0])
        del ar2[0]
    return new

if __name__ == "__main__":
    data = np.loadtxt("data.txt").tolist()
    data = merge(data)
    print data
