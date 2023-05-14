# Complete the can_make_pasta function to
# * Return true if the ingredients list contains
#   "flour", "eggs", and "oil"
# * Otherwise, return false
#
# The ingredients list will always contain three items.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.


from typing import List


def can_make_pasta(ingredients: List[str]):
#define can_make_pasta that passes a list
  return ["flour", "eggs", "oil"] == ingredients
    #if list has "flour", "eggs", and "oil"

    #return True

    #else return False
#print(can_make_pasta(ingredients))
print(can_make_pasta(["parsley", "oil", "potato"]))
print(can_make_pasta(["flour", "eggs", "oil"]))