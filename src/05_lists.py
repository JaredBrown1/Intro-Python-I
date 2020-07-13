# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
# x.append()
# # print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
y.remove(8)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
# x.append()
# print(x)

# def add_99(x):
#     del x[4]
#     del x[-1]
#     x.append(99)
#     x.append(10)
#     return x

# Print the length of list x
# YOUR CODE HERE
print(len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE


def mult_x(x):
    for num in x:
        print(num * 1000)


mult_x(x)
