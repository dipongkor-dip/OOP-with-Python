# function
# def add(x):
#     return x * 2


# defining a lambda function
mul = lambda x: x * x


sum = lambda x, y: x + y


result = mul(5)  # Output: 25
result_sum = sum(5, 3)  # Output: 8


numbers = [10, 11, 13, 15, 20, 25]

# squared_numbers = map(mul, numbers)  # Output: [25, 121, 169, 225, 400, 625]
# alternatively, you can use a lambda function directly in the map function
squared_numbers = map(
    lambda x: x * x, numbers
)  # Output: [100, 121, 169, 225, 400, 625]
# print(list(squared_numbers))

students = [
    {"name": "John", "age": 20},
    {"name": "Alice", "age": 22},
    {"name": "Bob", "age": 19},
    {"name": "Eve", "age": 21},
    {"name": "Charlie", "age": 23},
]

junior_students = filter(
    lambda s: s["age"] <= 20, students
)  # Output: [{'name': 'Bob', 'age': 19}]

print(list(junior_students))
