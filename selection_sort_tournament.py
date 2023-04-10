#!/bin/python


import time

def sorting(array):


    n = 0
    t1 = time.time()


    for i in range(1,len(array) + 1):

        array_subset = array[n:]

        min_element = min(array_subset)

        min_element_loc = array.index(min_element)

        array[n], array[min_element_loc] = array[min_element_loc], array[n]

        n = n + 1


    t2 = time.time()
    working_time = t2 - t1

    return 'sorted array:', array, "working time: ", working_time


