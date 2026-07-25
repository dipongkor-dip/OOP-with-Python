def full_name(first, last):
    name = f"full name is : {first} {last}"
    return name


# name = full_name("agr", "ali")
# print(name)


# def famous(**kargs)
def famous_name(first, last, **addition):
    name = f"{first} {last}"

    # print(addition)
    # print(addition['title'])

    for key, value in addition.items():
        print(f"{key} {value}")

    return name


name = famous_name(first="tina", last="saki", title="Kan", des="ban")
# print(name)


def a_lot(n1, n2):
    sum = n1 + n2
    mul = n1 * n2
    remain = n1 - n2
    return sum, mul, remain  # tuple
    # return [sum, mul, remain] # list


every = a_lot(55, 21)
# print(every)
