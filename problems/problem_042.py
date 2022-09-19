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


# Create an empty list to append to
# Create a variable that is a zip of the two lists
# Loop over each element in the zipped list, and add the numbers to each other
# Must use two variables in for loop to append over both values


def pairwise_add(list1, list2):
    list3 = []
    zipped_lists = zip(list1, list2)

    for x, y in zipped_lists:
        list3.append(x + y)

    return list3


print(pairwise_add([1, 2, 3, 4], [4, 5, 6, 7]))
print(pairwise_add([100, 200, 300], [10, 1, 180]))
