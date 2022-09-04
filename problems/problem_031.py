# Complete the sum_of_squares function which accepts
# a list of numerical values and returns the sum of
# each item squared
#
# If the list of values is empty, the function should
# return None
#
# Examples:
#   * [] returns None
#   * [1, 2, 3] returns 1*1+2*2+3*3=14
#   * [-1, 0, 1] returns (-1)*(-1)+0*0+1*1=2
#
# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

# loop over the list of numbers
# multiply each number by itself
# add the result of each index to the next


def sum_of_squares(values):
    if len(values) == 0:
        return None

    sum = 0

    for value in values:
        value *= value
        sum += value

    return sum


print(sum_of_squares([1, 2, 3]))
print(sum_of_squares([-1, 0, 1]))
print(sum_of_squares([4, 5, 6]))
