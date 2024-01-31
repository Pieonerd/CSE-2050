import time


def find_pairs_naive(lst, target):
    """Iterates over a lists using two nested loops to check for pairs that add up to the target"""
    pairs = set()                       # 1
    for a, num1 in enumerate(lst):      # n
        for num2 in lst[a+1:]:          # n
            if num1 + num2 == target:   # 1
                pair = num1, num2       # 1
                pairs.add(pair)         # 1
    return pairs                        # 1
                                        # ---------
                                        # 1 + n * n * 1 * 1 * 1 + 1 = O(n^2)
                                        # O(n^2) represents quadratic function, thus longer run time when n is greater
                                        # Exponential growth observed when n becomes greater

def find_pairs_optimized(lst, target):
    """
    Function that does the same thing as find_pairs_naive
    But uses a dictionary in order to improve the time complexity of the algorithm
    """
    indices = {}                                # 1
    pairs = set()                               # 1
    for i, num in enumerate(lst):               # n
        if num not in indices:                  # 1
            complement = target - num           # 1
            if complement in indices:           # 1
                pairs.add((complement, num))    # 1
            indices[num] = i                    # 1
    return pairs                                # 1
                                                #----------
                                                # 1 + 1 + n * 1 * 1 * 1 * 1 * 1 + 1 = O(n)
                                                # O(n) represents a linear relationship, thus more optimized than a quadratic relationship
                                                # The number of operations does not grow exponentially as n increases
 
def measure_min_time(fn, args):
    """Measures the minimum time of 10 runs for both functions using the time module"""
    minimum = float('inf')
    for i in range(10):
        start = time.time()
        fn(*args)
        end = time.time()
        if minimum > (end - start):
            minimum = (end - start)
    return minimum



if __name__ == '__main__':
    """A short loop that uses measure_min_time to print out a table showing the time taken for both functions as n increases"""
    print(f'n{"":<10}naive{"":<10}optimized{"":<10}')
    print('*'*40)
    n_list = [10, 50, 100, 150, 200, 300, 500]
    for n in n_list:
        arr = list(range(n))
        target = n
        naive_time = measure_min_time(find_pairs_naive, (arr, target))
        optimized_time = measure_min_time(find_pairs_optimized, (arr, target))
        print(f'{n:<11}{naive_time:<15.4f}{optimized_time:.4f}')
    print('-'*40)