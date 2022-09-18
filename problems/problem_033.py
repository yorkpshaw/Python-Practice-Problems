# Complete the sum_of_first_n_even_numbers function which
# accepts a numerical count n and returns the sum of the
# first n even numbers
#
# If the value of the limit is less than 0, then it should
# return None
#
# Examples:
#   * -1 returns None
#   * 0 returns 0
#   * 1 returns 0+2=2
#   * 2 returns 0+2+4=6
#   * 5 returns 0+2+4+6+8+10=30
#
# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.


def sum_of_first_n_even_numbers(n):
    if n < 0:
        return None

    count = 0

    for number in range(n + 1):
        count += number * 2

    return count


print(sum_of_first_n_even_numbers(1))
print(sum_of_first_n_even_numbers(2))
print(sum_of_first_n_even_numbers(5))
