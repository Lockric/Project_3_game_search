def MergeSort(list, l, r):
    if l < r:
        # get mid point
        m = l+(r-l)//2

        # merge sort left region
        MergeSort(list, l, m)

        # merge sort right region
        MergeSort(list, m+1, r)
        merge(list, l, m, r)

def merge(list, l, m, r):
    # get partitions of regon left and right
    n1 = m - l + 1
    n2 = r - m

    # define arrays to store partitions
    L = []
    R = []

    # fill out partition left
    for i in range(0, n1):
        L.append(list[l+i])

    # fill out partition right
    for i in range(0, n2):
        R.append(list[m + 1 + i])
    
    # 
    i = 0
    j = 0
    k = l

    # organize left and right partitions back into the list
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            list[k] = L[i]
            i += 1
        else:
            list[k] = R[j]
            j += 1
        k += 1
    
    # insert any remaining L nodes
    while i < n1:
        list[k] = L[i]
        i += 1
        k += 1
 
    # insert any remaining R nodes
    while j < n2:
        list[k] = R[j]
        j += 1
        k += 1