# create a new list, with a lambda as an element
my_list = ['test_string', 99, lambda x: x ** 2]
# access the value in the list
print(my_list[2])  # will print a lambda object stored in memory
# invoke the lambda function, passing in 5 as the argument
print(my_list[2](5))

# define a function that takes one input that is a function


def invoker(callback):
    # invoke the input pass the argument 2
    print(callback(2))


invoker(lambda x: 2 * x)
invoker(lambda y: 5 + y)
