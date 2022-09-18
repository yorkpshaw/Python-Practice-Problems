# Write a function that meets these requirements.
#
# Name:       num_concat
# Parameters: two numerical parameters
# Returns:    the concatenated string conversions
#             of the numerical parameters
#
# Examples:
#     input:
#       parameter 1: 3
#       parameter 2: 10
#     returns: "310"
#     input:
#       parameter 1: 9238
#       parameter 2: 0
#     returns: "92380"


# Convert each number to a
# string and add them together


def num_concat(num1, num2):
    string_num1 = str(num1)
    string_num2 = str(num2)

    string_number = string_num1 + string_num2

    return string_number


print(num_concat(3, 10))
print(num_concat(9238, 0))
