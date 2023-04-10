#!/bin/python3

import time


# funkcja do wyznaczania minimalnego elementu ciągu
# funkcja stosuje wyszukiwanie liniowe

def minimum(array):
    min_val = array[0]

    for i in range(1,len(array)):

        if array[i] < min_val:

            min_val = array[i]

    return min_val




# funkcja implementująca sortowanie przez wstawianie

def sorting(array):
    
    t1 = time.time()
   
    n = 0

    print('initial array: ', array)
    print('__________________________________________')

    for i in range(1,len(array) + 1):

        array_subset = array[n:]

        min_element = minimum(array = array_subset)

        min_element_loc = array.index(min_element)

        array[n], array[min_element_loc] = array[min_element_loc], array[n]

        n = n + 1

    t2 = time.time()
    work_time = t2-t1

    return 'sorted array:', array, "work time: ", work_time

