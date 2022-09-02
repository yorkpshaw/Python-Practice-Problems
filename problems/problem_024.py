# Complete the calculate_average function which accepts
# a list of numerical values and returns the average of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#
# Pseudocode is available for you


def calculate_average(values):
    if len(values) == 0:
        return None
    total = 0
    for value in values:
        total += value
        avg = total / len(values)

    return avg


print(calculate_average([1, 2, 3, 4, 5]))
print(calculate_average([5, 9, 10, 17, 25]))
print(calculate_average([5, 5, 5, 5, 5]))
