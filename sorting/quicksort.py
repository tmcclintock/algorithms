"""
My implementation of the quicksort algorithm.
"""
from swap import *
import numpy as np

def quicksort(array, lo=0, hi=None):
    #First call doesn't know the length
    if hi == None: hi = len(array)-1

    #Base case
    if lo >= hi: return array

    #Pick a pivot and partition
    pivot = hi
    pivot_value = array[pivot]
    N = lo
    for i in range(lo, hi):
        if array[i] <= array[pivot]:
            swap(array, i, N)
            N += 1
    swap(array, N, pivot)

    #Continue with other calls
    array = quicksort(array, lo, N-1)
    array = quicksort(array, N+1, hi)
    return array
        

if __name__ == "__main__":
    data = np.loadtxt("data.txt")
    print data
    data = quicksort(data)
    print data
