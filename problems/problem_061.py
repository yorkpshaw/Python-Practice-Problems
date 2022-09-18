# Write a function that meets these requirements.
#
# Name:       remove_duplicates
# Parameters: a list of values
# Returns:    a copy of the list removing all
#             duplicate values and keeping the
#             original order
#
# Examples:
#     * input:   [1, 1, 1, 1]
#       returns: [1]
#     * input:   [1, 2, 2, 1]
#       returns: [1, 2]
#     * input:   [1, 3, 3, 20, 3, 2, 2]
#       returns: [1, 3, 20, 2]


def remove_duplicates(values):
    noduplicates = []

    for char in values:
        if char not in noduplicates:
            noduplicates.append(char)

    return noduplicates


print(remove_duplicates([1, 1, 1, 1]))
print(remove_duplicates([1, 2, 2, 1]))
print(remove_duplicates([1, 3, 3, 20, 3, 2, 2]))
