def partition(list, size):
    chunks = []
    in_progress = []
    for item in list:
        if len(in_progress) == size:
            chunks.append(in_progress)
            in_progress = []
        in_progress.append(item)
    return chunks


input = [0, 1, 2, 3, 4, 5, 6]
result = partition(input, 2)
print(result)


# Please complete the pair_up function below so that it
# takes a list of items and returns a list of pairs
# of consecutive items.


def pair_up(items):
    pairs = []
    for index in range(0, len(items), 2):
        if index + 1 < len(items):
            pair = [items[index], items[index + 1]]
            pairs.append(pair)
    return pairs
