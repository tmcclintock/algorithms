"""
My implementation of the binary search algorithm. This algorithm works only on sorted arrays.
"""
import numpy as np

def binarysearch(num, array, lo=0, hi=None):
    N = len(array)

    #First call
    if hi == None: hi = N

    #Number not found
    if lo >= hi:
        print "Number not found. Returning -1 as an index."
        return -1
    
    mid = lo + (hi-lo)/2
    #print lo, mid, hi
    if array[mid] == num: return mid
    elif array[mid] > num: return binarysearch(num, array, lo, mid)
    #array[mid] < num:
    return binarysearch(num, array, mid+1, hi)
    

if __name__ == "__main__":
    #Create a sorted list of integers
    np.random.seed(123456789)
    data = np.random.randint(low=0, high=1000, size=100)
    data = np.sort(data)

    number = data[np.random.randint(low=0, high=100, size=1)][0]
    print "Finding the number: ", number
    index = binarysearch(number, data)
    print "Found at index: ", index
