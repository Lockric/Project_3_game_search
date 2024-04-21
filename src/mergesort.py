# Used this file to create the merge sort https://www.w3schools.com/dsa/dsa_algo_mergesort.php

def MergeSort(my_list, l, r):
    if l < r:
        # get mid point
        m = l+(r-l)//2

        # merge sort left region
        MergeSort(my_list, l, m)

        # merge sort right region
        MergeSort(my_list, m+1, r)
        merge(my_list, l, m, r)

def merge(my_list, l, m, r):
    # get partitions of regon left and right
    n1 = m - l + 1
    n2 = r - m

    # define arrays to store partitions
    L = my_list[l : l + n1]
    R = my_list[m + 1 : m + 1 + n2]
    
    # 
    i = 0
    j = 0
    k = l

    # organize left and right partitions back into the list
    while i < n1 and j < n2:
        if L[i].rating >= R[j].rating:
            my_list[k] = L[i]
            i += 1
        else:
            my_list[k] = R[j]
            j += 1
        k += 1
    
    # insert any remaining L nodes
    while i < n1:
        my_list[k] = L[i]
        i += 1
        k += 1
 
    # insert any remaining R nodes
    while j < n2:
        my_list[k] = R[j]
        j += 1
        k += 1