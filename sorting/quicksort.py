"""
My implementation of the quicksort algorithm.
"""
from swap import *
import numpy as np

def quicksort(array, lo=0, hi=None):
    #First call doesn't know the length
    if hi == None: hi = len(array)

    #Base case
    if lo >= hi: return array

    #Pick a pivot and sort on that pivot
    left  = []
    right = []
    pivot = lo
    pivot_value = array[pivot]
    for i in range(lo, hi):
        if i == pivot: continue
        if array[i] <= pivot_value: 
            left.append(array[i])
        else:
            right.append(array[i])
    left.append(pivot_value)
    NL = len(left)
    array[lo: lo+NL] = left
    array[lo+NL: hi] = right

    #Continue with other calls
    print lo, lo+NL, hi, pivot_value, left, right, array
    #array = quicksort(array, lo, lo+NL)
    #array = quicksort(array, lo+NL+1, hi)
    return array
        

if __name__ == "__main__":
    data = np.loadtxt("data.txt")[:6]
    print data
    data = quicksort(data)
    #print data
