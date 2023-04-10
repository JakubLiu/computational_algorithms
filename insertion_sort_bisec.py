#!/bin/python


import time
import bisect

def insertion_sort_bisect(array):

    t1 = time.time()

    sorted_part = []

    for element in array:
        bisect.insort(sorted_part, element)
    
    t2 = time.time()
    work_time = t2 - t1

    return 'sorted array: ', sorted_part, 'work time: ', work_time

print(insertion_sort_bisect(array = [10,4,2]))




