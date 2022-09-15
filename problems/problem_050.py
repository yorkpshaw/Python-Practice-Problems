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


def halve_the_list(single_list):
    list1 = []
    list2 = []
    if len(single_list) % 2 == 0:
        mid = len(single_list) // 2
        list1 = single_list[:mid]
        list2 = single_list[mid:]
    if len(single_list) % 2 != 0:
        mid = (len(single_list) // 2) + 1
        list1 = single_list[:mid]
        list2 = single_list[mid:]

    return list1, list2


print(halve_the_list([1, 2, 3, 4, 5, 6]))

print(halve_the_list([1, 2, 3, 4, 5, 6, 7]))

# divide the length of the list by 2
# round up that number
# append to a list
