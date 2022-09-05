# Write a function that meets these requirements.
#
# Name:       only_odds
# Parameters: a list of numbers
# Returns:    a copy of the list that only includes the
#             odd numbers from the original list
#
# Examples:
#     * input:   [1, 2, 3, 4]
#       returns: [1, 3]
#     * input:   [2, 4, 6, 8]
#       returns: []
#     * input:   [1, 3, 5, 7]
#       returns: [1, 3, 5, 7]


def only_odds(num_list):
    empty_list = []
    for odd_num in num_list:
        if odd_num % 2 == 1:
            empty_list.append(odd_num)
    return empty_list


print(only_odds([1, 2, 3, 4]))
print(only_odds([2, 4, 6, 8]))
print(only_odds([1, 3, 5, 7]))
