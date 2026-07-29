# function is a first class object


def double_decker():
    print("Starting the double decker")

    def inner_fun():
        print("inside the inner")
        return 5000

    return inner_fun


# print(double_decker()) # return function
# print(double_decker()())


def do_something(work):
    print("working now")
    # print(work)
    work()
    print("working end")


# do_something(5)
# do_something("String given")


def coding():
    print("coding in python")


do_something(coding)
