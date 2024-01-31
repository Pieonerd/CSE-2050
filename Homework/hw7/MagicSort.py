from math import log2

def linear_scan(L, invoked_algos=set()):
    "Keeps track of the following edge cases"
    # Sorted list edge case
    if not any(L[i] > L[i+1] for i in range(len(L)-1)):
        return 'sorted'
    
    # Reverse list edge case
    if not any(L[i] < L[i+1] for i in range(len(L)-1)):
        invoked_algos.add('reverse_list')
        reverse_list(L)
        return 'reverse_list'

    # At most 5 items out of place edge case
    not_sorted = 0
    for i in range(len(L)-1):
        if L[i] > L[i+1]:
            not_sorted += 1
    if not_sorted <= 5:
        invoked_algos.add('insertionsort')
        insertionsort(L)
        return 'insertionsort'
    
def reverse_list(L):
    "Reverses a list in linear time"
    for i in range(len(L) // 2):
        L[i], L[len(L)-i-1] = L[len(L)-i-1], L[i]

def insertionsort(L, left=0, right=None):
    "Sorts L in place using insertion sort"
    if right is None:
        right = len(L)
    n = right - left
    for i in range(n):
        for j in range(left+1, right):
            if L[j-1] > L[j]:
                L[j], L[j-1] = L[j-1], L[j]


def quicksort(L, left=0, right=None, depth=0, invoked_algos=set()):
    "Sorts L in place using quick sort"
    if right is None:
        right = len(L)

    # Sort using insertion sort for small sublists
    if right - left <= 16:
        invoked_algos.add('insertionsort')
        insertionsort(L, left, right)
        return invoked_algos
        
    if right - left > 1:
        # Check depth
        if depth > (2 * log2(len(L))+1):
            invoked_algos.add('mergesort')
            mergesort(L)
            return invoked_algos
        
        # Divide
        mid = partition(L, left, right)

        # Conquer
        invoked_algos_left = quicksort(L, left, mid, depth+1, invoked_algos)
        invoked_algos_right = quicksort(L, mid+1, right, depth+1, invoked_algos)
        invoked_algos.update(invoked_algos_left)
        invoked_algos.update(invoked_algos_right)
        invoked_algos.add('quicksort')
        return invoked_algos

def partition(L, left, right):
    "Returns the index of the pivot point"
    pivot = right - 1
    i = left        # index in left half
    j = pivot - 1   # index in right half

    while i < j:
        # Move i to point to an element >= L[pivot]
        while L[i] < L[pivot]:
            i = i + 1

        # Move j to point an element < L[point]
        while i < j and L[j] >= L[pivot]:
            j = j - 1

        # Swap elements i and j if i < j
        if i < j:
            L[i], L[j] = L[j], L[i]

    # Put the pivot in place
    if L[pivot] <= L[i]:
        L[pivot], L[i] = L[i], L[pivot]
        pivot = i
        
    # Return the index of the pivot
    return pivot

def mergesort(L):
    "Sorts L in place using merge sort"
    # Base case
    if len(L) < 2:
        return
    
    # Use insertion sort for small sublists
    if len(L) <= 16:
        insertionsort(L)
        return
    
    # Divide
    mid = len(L) // 2
    A = L[:mid]
    B = L[mid:]

    # Conquer
    mergesort(A)
    mergesort(B)
    
    # Combine
    merge(A, B, L)

def merge(A, B, L):
    "Merges sorted lists A and B into L"
    i = 0   # index into A
    j = 0   # index into B
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            L[i+j] = A[i]
            i += 1
        else:
            L[i+j] = B[j]
            j += 1
    # Add any remaining elements once the list is empty
    L[i+j:] = A[i:] + B[j:]
   
def magic_sort(L):
    "Sorts L in place using a combination of sorting algorithms"
    invoked_algos = set()
    scan = linear_scan(L, invoked_algos)
    if scan is not None:
        invoked_algos.add(scan)
    else:
        invoked_algos = quicksort(L, 0, len(L), 0, invoked_algos)
    return invoked_algos
 