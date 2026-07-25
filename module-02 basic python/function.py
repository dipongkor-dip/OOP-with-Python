# define
def mul_fn(num):
    result = num * 2
    print(result)


# mul_fn(4)


def sum_fn(a, b, c=0):
    total = a + b + c
    return total


# result = sum_fn(5, 6)
# print(result)


# args
def total_sum(*numbers):  # it's tuple or star args
    # print(numbers)  # tuple like an array
    total = 0
    for num in numbers:
        # print(num)
        total += num
    return total


total = total_sum(1, 2, 3, 4, 5)
# print(total)
