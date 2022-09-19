# Write a function that meets these requirements.
#
# Name:       generate_lottery_numbers
# Parameters: none
# Returns:    a list of six random unique numbers
#             between 1 and 40, inclusive
#
# Example bad results:
#    [4, 2, 3, 3, 1, 5] duplicate numbers
#    [1, 2, 3, 4, 5] not six numbers
#
# You can use randint from random, here, or any of
# the other applicable functions from the random
# package.
#
# https://docs.python.org/3/library/random.html


# create an empty list variable
# while the len of the variable is less than the number of numbers in the list,
# generate a random number to append if not in the list

from random import randint


def generate_lottery_numbers():
    lotto = []
    while len(lotto) < 6:
        random_number = randint(1, 40)
        if random_number not in lotto:
            lotto.append(random_number)

    return lotto


print(generate_lottery_numbers())
