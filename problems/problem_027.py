# Complete the max_in_list function to find the
# maximum value in a list
#
# If the list is empty, then return None.
#


def max_in_list(values):
    if len(values) == 0:
        return None

    return max(values)


print(max_in_list([5, 6, 100, 1, 4]))
