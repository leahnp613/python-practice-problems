# Complete the fizzbuzz function to return
# * The word "fizzbuzz" if number is evenly divisible by
#   by both 3 and 5
# * The word "fizz" if number is evenly divisible by only
#   3
# * The word "buzz" if number is evenly divisible by only
#   5
# * The number if it is not evenly divisible by 3 nor 5
#
# Try to combine what you have done in the last two problems
# from memory.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.


def fizzbuzz(number):
    # define the function fizzbuzz
    # if a number is divisible by both 3 and 5
    if number % 3 == 0 and number % 5 == 0:
        # return "fizzbuzz"
        return "fizzbuzz"
    # if number is divisible only by 3
    if number % 3 == 0:
        # return "fizz"
        return "fizz"
    # if number is divisible only by 5
    if number % 5 == 0:
        # return "buzz"
        return "buzz"

    # return number if not divisible by either, simple return
    return number
    # call fizzbuzz(15) and print it


print(fizzbuzz(15))
