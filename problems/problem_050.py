# Write a function that meets these requirements.
#
# Name:       halve_the_list
# Parameters: a single list
# Returns:    two lists, each containing half of the original list
#             if the original list has an odd number of items, then
#             the extra item is in the first list
#
# Examples:
#    * input: [1, 2, 3, 4]
#      result: [1, 2], [3, 4]
#    * input: [1, 2, 3]
#      result: [1, 2], [3]


def halve_the_list(singlelist):
    list1 = []
    list2 = []
    mid = (len(singlelist) // 2) + 1
    list1 = singlelist[:mid]
    list2 = singlelist[mid:]

    return list1, list2


print(halve_the_list([1, 2, 3, 4]))
print(halve_the_list([1, 2, 3]))


# create two empty list variables
# we want to return two lists cut in half
# get the length of the list and divide it by two
# return two lists
