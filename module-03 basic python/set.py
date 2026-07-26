# list --> []
# tuple --> ()
# set --> {} == unique items collection . No duplicate

numbers = [1, 2, 3, 4, 5, 4, 3, 2, 1]

# print(numbers)

numbers_set = set(numbers)

numbers_set.add(10)
numbers_set.remove(5)
# numbers_set[1] = 11 # index sequence not maintain

# if 1 & 3 in numbers_set: print("exist")
# if 1 | 3 in numbers_set: print("exist")

# for i in numbers_set:
#     print(i)

A = {1, 3, 5}
B = {2, 3, 6, 9}

print(A & B) # {3}
print(A | B) # {1, 2, 3, 5, 6, 9}

# print(numbers_set)
