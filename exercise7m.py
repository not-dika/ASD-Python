import numpy as np

def avg(arr):
    return np.mean(arr)

def min(arr):
    return np.min(arr)

def max(arr):
    return np.max(arr)

def abv_avg(arr):
    return sum(arr > avg(arr))

