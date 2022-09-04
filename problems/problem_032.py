# Complete the sum_of_first_n_numbers function which accepts
# a numerical limit and returns the sum of the numbers from
# 0 up to and including limit.
#
# If the value of the limit is less than 0, then it should
# return None
#
# Examples:
#   * -1 returns None
#   * 0 returns 0
#   * 1 returns 0+1=1
#   * 2 returns 0+1+2=3
#   * 5 returns 0+1+2+3+4+5=15
#
# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

#


def sum_of_first_n_numbers(limit):
    if limit < 0:
        return None

    num = 0

    for n in range(limit + 1):
        num += n

    return num


print(sum_of_first_n_numbers(0))
print(sum_of_first_n_numbers(1))
print(sum_of_first_n_numbers(2))
print(sum_of_first_n_numbers(5))
print(sum_of_first_n_numbers(-1))
print(sum_of_first_n_numbers(10))
