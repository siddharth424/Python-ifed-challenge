import time
import pandas as pd
import numpy as np

def by_Numpy(subset_elements,all_elements):
    
    #starting of function
    start = time.time()

    #Getting all the common elements using intersection1d
    verified_elements= np.intersect1d(subset_elements, all_elements)


    # print number of elements common and time taken
    print(len(verified_elements))
    print('Duration: {} seconds'.format(time.time() - start))


by_Numpy.__doc__ = """
This function finds number of common value from two lists using numpy
 """
 

def bySets(subset_elements,all_elements):
    #start of the function
    start = time.time()

    #convert lists to sets
    a =set(subset_elements)
    b =set(all_elements)

    #find the elements in intersection of sets
    verified_elements = a.intersection(b)

    # print number of elements common and time taken
    print(len(verified_elements))
    print('Duration: {} seconds'.format(time.time() - start))


bySets.__doc__ = """
This function finds number of common value from two lists by converting them to sets and finding number of intersection.
 """
