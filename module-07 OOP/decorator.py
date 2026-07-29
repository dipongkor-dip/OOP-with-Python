def timer(func):
    def inner():
        print("Time Started")

        func()

        print("Time ended")

    return inner


# timer()()


# def get_factorial():
#     print("factorial function")

# timer(get_factorial)()


# alternative
@timer  # as a decorator
def get_factorial():
    print("factorial function")


get_factorial()
