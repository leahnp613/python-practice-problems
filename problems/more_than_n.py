# Create a fxn named “more_than_n” that has three parameters: a list, an item, and a number. The fxn should return “True” if the item appears more then the number of times specified. Otherwise, the fxn should return “False”.

# Input: ([2,4,6,2,3,2,1,2], 2, 3) => Output: True
# Input: ([2,4,6,2,3,2,1,2], 4, 3) => Output: False


def more_than_n:(list_1, item, number):
    number = int(number)
    if item > number:
        return True
        