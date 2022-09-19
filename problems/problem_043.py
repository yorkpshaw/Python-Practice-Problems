# Complete the find_indexes function which accepts two
# parameters, a list and a search term. It returns a new
# list that contains the indexes of the search term in
# the search list.
#
# Remember that indexes in Python are zero-based. That
# means the first element in the list is index 0.
#
# Examples:
#   * search_list:  [1, 2, 3, 4, 5]
#     search_term:  4
#     result:       [3]
#   * search_list:  [1, 2, 3, 4, 5]
#     search_term:  6
#     result:       []
#   * search_list:  [1, 2, 1, 2, 1]
#     search_term:  1
#     result:       [0, 2, 4]
#
# Look up the enumerate function to help you with this problem.


# Create an empty list variable to contain indices,
# Return that variable at the end

# Use the enumerate function to return a list of the index with key
# You can also enumerate on first line of a for loop...
# No need for extra variable

# If the value of the second number is equal to parameter,
# append the first number (index) to the empty variable.

# return the index of the list


def find_indexes(search_list, search_term):
    idx_value = []
    idx_list = enumerate(search_list)

    for idx, number in idx_list:
        if number == search_term:
            idx_value.append(idx)

    return idx_value


print(find_indexes([1, 2, 3, 4, 5], 4))
print(find_indexes([1, 2, 3, 4, 5], 6))
print(find_indexes([1, 2, 1, 2, 1], 1))
