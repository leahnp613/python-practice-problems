# DOUBLE INDEX:
# Create a fxn named “double_index” with two parameters: a list and an index number. The fxn should double the value of the list element at the specified index and return the list with the doubled value.
# If the index is not a valid index, the fxn should return the original list.

# Input: ([3,8,-10,12], 2) => Output: [3,8,-20,12]
# Input: ([3,8,-10,12], 6) => Output: [3,8,-10,12]


import typing


def double_index(list_1: typing.List[int], index: int):
    try:
        list_1[index] = 2 * list_1[index]
    except IndexError:
        return list_1
    return list_1


print(double_index([3, 8, -10, 12], 2))
print(double_index([3, 8, -10, 12], 10))
