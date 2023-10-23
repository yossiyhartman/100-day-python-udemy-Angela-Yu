list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [3, 2, 3, 6, 5, 8, 9]

print([x for x, y in zip(list1, list2) if x == y])
