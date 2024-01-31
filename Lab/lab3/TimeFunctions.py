import time


def time_function(func, args, n_trials=10):
    """Returns the number of seconds to run func with args"""
    minimum = float('inf')
    for i in range(n_trials):
        start = time.time()
        func(args)
        end = time.time()
        if (end - start) < minimum:
            minimum = end - start
    
    return minimum
    
def time_function_flexible(f, args, n_trials=10):
    """
    Returns the number of seconds to run func with args
    Unpacks args into separate arguments
    """
    minimum = float('inf')
    for i in range(n_trials):
        start = time.time()
        f(*args)
        end = time.time()
        if (end - start) < minimum:
            minimum = end - start
    return minimum

def add_2_nums(p1, p2):
    return p1 + p2

def add_3_nums(p1, p2, p3):
    return p1 + p2 + p3


if __name__ == '__main__':
    # Some tests to see if time_function works
    def test_func(L):
        for item in L:
            item *= 2

    L1 = [i for i in range(10**5)]
    t1 = time_function(test_func, L1)

    L2 = [i for i in range(10**6)] # should be 10x slower to operate on every item
    t2 = time_function(test_func, L2)

    print("t(L1) = {:.3g} ms".format(t1*1000))
    print("t(L2) = {:.3g} ms".format(t2*1000))