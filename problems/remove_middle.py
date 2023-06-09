# REMOVE MIDDLE:
# Create a fxn named “remove_middle” which has three parameters: a list, a start number, an end number. The fxn should return a sub-list of the list containing all of the elements between the start and end indexes.

# Input: ([4,8,15,16,23,42], 1, 3]) => Output: [8,15,16]


def remove_middle(base_list, start_number, end_number):
    result = base_list[start_number : end_number + 1]
    return result


list_1 = [4, 8, 15, 16, 23, 42]
print(remove_middle(list_1, 1, 3))
