import math
import time


def timer(func):
    def inner(*args, **kwargs):
        start = time.time()

        func(*args, **kwargs)

        end = time.time()

        print("total time taken:", (end - start))

    return inner


@timer  # as a decorator
def get_factorial(n):
    print("factorial function")

    res = math.factorial(n)

    print(f"factorial of {n} is : ", res)


get_factorial(5)  # args
get_factorial(n=5)  # key value = kwargs


# factorial is = n!
# 5 factorial = 5! = 5 * 4 * 3 * 2 * 1 = 120
