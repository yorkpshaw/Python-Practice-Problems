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


# create an empty list variable to return
# loop over the parameter
# split the list in the variable passed in the loop
# create a count variable set to 0
# this is so it doesn't keep resetting inside the next loop
# loop over the split list
# convert each element in the split list to an integer
# increment the count variable by the converted integer
# append the numbers to the result list


def add_csv_lines(csv_lines):

    result = []

    for csv in csv_lines:
        lines = csv.split(",")
        count = 0
        for line in lines:
            new_num = int(line)
            count += new_num
        result.append(count)

    return result


print(add_csv_lines(["8,1,7", "10,10,10", "1,2,3"]))
print(add_csv_lines([]))
print(add_csv_lines(["3", "1,9"]))
