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

    count = 0
    for value in values:
        count += value
        average = count / len(values)

    return average


print(calculate_average([10, 10, 20, 20, 30, 30]))
