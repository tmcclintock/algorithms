"""
I implement the bubble sort.
"""
import numpy as np
from swap import *

def bubble(array):
    N = len(array)
    while True:
        is_sorted = True
        for i in xrange(0, N-1):
            if array[i] > array[i+1]:
                swap(array, i, i+1)
                is_sorted = False
        if is_sorted: break
    return

if __name__ == "__main__":
    data = np.loadtxt("data.txt")
    bubble(data)
    print data
