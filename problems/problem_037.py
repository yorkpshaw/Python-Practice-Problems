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


# append the result by length - length of number amount of times
# append number to that afterwards


def pad_left(number, length, pad):

    omg = str(number)

    while len(omg) < length:
        omg = pad + omg

    return omg


print(pad_left(10, 4, "*"))
print(pad_left(10, 5, "0"))
print(pad_left(1000, 3, "0"))
print(pad_left(19, 5, "-"))
print(pad_left(7777, 7, "#"))
print(pad_left(555, 7, "^"))
