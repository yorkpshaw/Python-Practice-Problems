# Complete the pad_left function which takes three parameters
#   * a number
#   * the number of characters in the result
#   * a padding character
# and turns the number into a string of the desired length
# by adding the padding character to the left of it
#
# Examples:
#   * number: 10
#     length: 4
#     pad:    "*"
#     result: "**10"
#   * number: 10
#     length: 5
#     pad:    "0"
#     result: "00010"
#   * number: 1000
#     length: 3
#     pad:    "0"
#     result: "1000"
#   * number: 19
#     length: 5
#     pad:    " "
#     result: "   19"


# Output returns a string
# Convert number to a string and stash it in a variable
# While the length of the number string is less than the length parameter,
# add the string pad + number string
# Pad needs to be on the left/right depending on placement


def pad_left(number, length, pad):
    numero = str(number)

    while len(numero) < length:
        numero = pad + numero

    return numero


print(pad_left(10, 4, "*"))
print(pad_left(10, 5, "0"))
print(pad_left(1000, 3, "0"))
print(pad_left(19, 5, " "))
