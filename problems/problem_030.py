# Complete the find_second_largest function which accepts
# a list of numerical values and returns the second largest
# in the list
#
# If the list of values is empty, the function should
# return None
#
# If the list of values has only one value, the function
# should return None
#
# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.


# if the list is empty, return none
# if the list only has one value (if length is one) return none
# sort the list in order
# pop the last value
# return the last value of list with -1


def find_second_largest(values):
    if len(values) <= 1:
        return None

    dupes = set(values)

    sorted_nums = list(sorted(dupes))

    return sorted_nums[-2]


print(find_second_largest([1, 5, 2, 6, 3, 6]))
print(find_second_largest([65, 10, 39, 104, 28, 104]))
print(find_second_largest([-1, -6, -2, -4, -2]))
