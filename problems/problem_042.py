# Complete the pairwise_add function which accepts two lists
# of the same size. It creates a new list and populates it
# with the sum of corresponding entries in the two lists.
#
# Examples:
#   * list1:  [1, 2, 3, 4]
#     list2:  [4, 5, 6, 7]
#     result: [5, 7, 9, 11]
#   * list1:  [100, 200, 300]
#     list2:  [ 10,   1, 180]
#     result: [110, 201, 480]
#
# Look up the zip function to help you with this problem.


# Use zip to combine the two lists.
# Iterate over the new list and add the corresponding indices
# list3


def pairwise_add(list1, list2):
    listzero = []

    for entry1, entry2 in zip(list1, list2):
        listzero.append(entry1 + entry2)

    return listzero


print(pairwise_add([1, 2, 3, 4], [4, 5, 6, 7]))
