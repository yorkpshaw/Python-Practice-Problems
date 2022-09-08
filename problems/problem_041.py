# Complete the add_csv_lines function which accepts a list
# as its only parameter. Each item in the list is a
# comma-separated string of numbers. The function should
# return a new list with each entry being the corresponding
# sum of the numbers in the comma-separated string.
#
# These kinds of strings are called CSV strings, or comma-
# sepearted values strings.
#
# Examples:
#   * input:  []
#     output: []
#   * input:  ["3", "1,9"]
#     output: [3, 10]
#   * input:  ["8,1,7", "10,10,10", "1,2,3"]
#     output:  [16, 30, 6]
#
# Look up the string split function to find out how to
# split a string into pieces.

# Write out your own pseudocode to help guide you.


def add_csv_lines(csv_lines):
    added_nums = []

    for lines in csv_lines:
        splitnums = lines.split(",")
        count = 0
        for numstring in splitnums:
            sumnum = int(numstring)
            count += sumnum
        added_nums.append(count)

    return added_nums


print(add_csv_lines(["1,12", "1,9", "33,1"]))


# create an empty list
# loop over the list
# convert each element to a number, split comma, set that to a new variable
# loop over the new variable
# create a varible
# add the numbers in the converted-to-num string
# append to the list
