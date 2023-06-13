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
    return max(value1, value2, value3)

print(max_of_three(1, 2, 3))
print(max_of_three(29, 12, 123))
print(max_of_three(3, 3, 1))