# Complete the is_palindrome function to check if the value in
# the word parameter is the same backward and forward.
#
# For example, the word "racecar" is a palindrome because, if
# you write it backwards, it's the same word.

# It uses the built-in function reversed and the join method
# for string objects.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

#set word to example palindrome
word = "racecar"


def is_palindrome(word):
    return word == word[::-1]


print(is_palindrome("racecar"))

#slice and join word and return new list
#if new list is == word then return True
#else return False
