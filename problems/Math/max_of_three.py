# Complete the max_of_three function so that returns the
# maximum of three values.
#
# If two values are the same maximum value, return either of
# them.
# If the all of the values are the same, return any of them
#
# Use the >= operator for greater than or equal to

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.


def max_of_three(value1, value2, value3):
    # find the max of the inputs
    return max([value1, value2, value3])
    # call the function


maximum = max_of_three(12, 18, 22)
# print
print(maximum)
