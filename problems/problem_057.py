# Write a function that meets these requirements.
#
# Name:       sum_fraction_sequence
# Parameters: a number
# Returns:    the sum of the fractions of the
#             form 1/2+2/3+3/4+...+number/number+1
#
# Examples:
#     * input:   1
#       returns: 1/2
#     * input:   2
#       returns: 1/2 + 2/3
#     * input:   3
#       returns: 1/2 + 2/3 + 3/4


def sum_fraction_sequence(num1):
    count = 0
    for number in range(1, num1 + 1):
        count += number / (number + 1)

    return count


print(sum_fraction_sequence(1))
print(sum_fraction_sequence(2))
print(sum_fraction_sequence(3))

# num1/num1+2 + num1+1/num1+2 etc.
# will need a for loop
