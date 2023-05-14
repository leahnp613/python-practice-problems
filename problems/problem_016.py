# Complete the is_inside_bounds function which takes an x
# coordinate and a y coordinate, and then tests each to
# make sure they're between 0 and 10, inclusive.


def is_inside_bounds(x, y):
  #define is_inside_bounds
  #if x =< 10 and x >= 0 and y <= 10 and y >= 0
    #return True
  if x <= 10 and x >= 0 and y <= 10 and y >= 0:
    return True
  else:
    return False
#print(is_inside_bounds(2,5))
print(is_inside_bounds(2,5))
print(is_inside_bounds(12,5))
