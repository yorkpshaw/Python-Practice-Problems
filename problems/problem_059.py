# Write a function that meets these requirements.
#
# Name:       specific_random
# Parameters: none
# Returns:    a random number between 10 and 500, inclusive,
#             that is divisible by 5 and 7
#
# Examples:
#     * returns: 35
#     * returns: 105
#     * returns: 70
#
# Guidance:
#   * Generate all the numbers that are divisible by 5
#     and 7 into a list
#   * Use random.choice to select one

import random


def specific_random():

    number_list = []

    for number in range(10, 500):
        if number % 5 == 0 and number % 7 == 0:
            number_list.append(number)

    random_number = random.choice(number_list)
    return random_number


print(specific_random())
