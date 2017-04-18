"""
I create random data to be sorted. I will just use a list of integers.
"""
import numpy as np
data = np.random.randint(0, 1000, size=100)
np.savetxt("data.txt",data)
