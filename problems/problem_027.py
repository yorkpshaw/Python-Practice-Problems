# Complete the max_in_list function to find the
# maximum value in a list
#
# If the list is empty, then return None.
#

# if len(values) == 0, return none
# loop over the list with a for loop
# create a variable which is the first index of the list
# if any numbers you loop over are bigger than that first number,
# then reassign that index to be the one
# if it's smaller, who cares


def max_in_list(values):

    if len(values) == 0:
        return None

    biggest_num = values[0]

    for dwade in values:
        if dwade > biggest_num:
            biggest_num = dwade

    return biggest_num


print(max_in_list([99, 8, 6, 101, 5, 7]))
