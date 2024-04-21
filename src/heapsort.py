# Used this as reference: https://www.geeksforgeeks.org/python-program-for-heap-sort/ 
def heapify(arr, n , i):
    # Initialize the largest as root
    largest = i
    # left, right
    left = 2 * i + 1
    right = 2 * i + 2
    # check if the left child of root exists and is greater than root
    if left < n and arr[i].rating < arr[left].rating:
        largest = left
     # check if the right child of root exists and is greater than root
    if right < n and arr[largest].rating < arr[right].rating:
        largest = right
    # change root when needed
    if largest != i:
        # swap!
        (arr[i], arr[largest]) = (arr[largest], arr[i])
    # use heapify :)
        heapify(arr, n, largest)

def HeapSort(arr):
    # CODE HERE 
    # NEED TO ADD WHAT WE ARE SEARCHING MAYBE!
    n = len(arr)
    for i in range (n // 2, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])
        heapify(arr, i, 0)
