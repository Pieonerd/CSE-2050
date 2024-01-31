# TODO: implement the 4 functions (as always, include docstrings & comments)

def find_zero(L):
    "return the index of the 0 in such a list in O(log(n))"
    # base case - empty list returns -1
    if len(L) == 0: return -1
    
    # calculate median
    median = len(L) // 2
    
    # base case - found the item
    if L[median] == 0: return median

    # item is in smaller half
    elif L[median] < 0:
        idx = find_zero(L[median+1:])
        return median+1+idx
    
    # item is in bigger half
    elif L[median] > 0: 
        idx = find_zero(L[0:median])
        return idx

    
def bubble(L, left, right):
    "Bubble sort algorithm"
    for i in range(left, right):
        keep_going = False
        for j in range(left, right-1):
            if L[j] > L[j+1]:
                keep_going = True
                # swaps items
                L[j+1], L[j] = L[j], L[j+1]

        if not keep_going: break

def selection(L, left, right):
    "Selection sort algorithm"
    for i in range(left, right):
        max_index = i
        for index in range(i, right):
            if L[index] < L[max_index]:
                max_index = index
        # swaps current element and max index
        L[i], L[max_index] = L[max_index], L[i]


def insertion(L, left, right):
    "Insertion sort algorithm"
    for i in range(left, right):
        for j in range(left, right-1):
            if L[j] > L[j+1]:
                # swaps items
                L[j], L[j+1] = L[j+1], L[j]



def sort_halfsorted(L, sort):
    '''Efficiently sorts a list comprising a series of negative items, a single 0, and a series of positive items
    
        Input
        -----
            * L:list
                a half sorted list, e.g. [-2, -1, -3, 0, 4, 3, 7, 9, 14]
                                         <---neg--->     <----pos----->

            * sort: func(L:list, left:int, right:int)
                a function that sorts the sublist L[left:right] in-place
                note that we use python convention here: L[left:right] includes left but not right

        Output
        ------
            * None
                this algorithm sorts `L` in-place, so it does not need a return statement

        Examples
        --------
            >>> L = [-1, -2, -3, 0, 3, 2, 1]
            >>> sort_halfsorted(L, bubble)
            >>> print(L)
            [-3, -2, -1, 0, 1, 2, 3]
    '''

    idx_zero = find_zero(L)     # find the 0 index 
    sort(L, 0, idx_zero)        # sort left half
    sort(L, idx_zero+1, len(L)) # sort right half