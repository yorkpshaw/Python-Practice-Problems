# Complete the calculate_sum function which accepts
# a list of numerical values and returns the sum of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#


def calculate_sum(values):
    if len(values) == 0:
        return None

    count = 0
    for value in values:
        count += value

    return count
