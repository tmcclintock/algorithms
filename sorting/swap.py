"""
This contains a custom swap method.
This will be imported into all sorting algorithms I implement.
"""
def swap(array,i,j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
    return
