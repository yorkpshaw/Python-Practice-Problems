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

# number/number+1 + number+2/number+3

# Create a count variable to return at the end
# Use range to loop numbers up to the parameter
# Range is 1 to parameter + 1 so it starts at 1 and not 0
# and includes the parameter
# increment sum count by number/number+1 which always goes up 1 each iteration


def sum_fraction_sequence(number):
    # count = 0
    # for numero in range(number + 1):
    #     count += numero / numero + 1
    # return count

    sum = 0
    for i in range(1, number + 1):
        sum += i / (i + 1)
    return sum


print(sum_fraction_sequence(1))
print(sum_fraction_sequence(2))
print(sum_fraction_sequence(3))
