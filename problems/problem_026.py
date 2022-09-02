# Complete the calculate_grade function which accepts
# a list of numerical scores each between 0 and 100.
#
# Based on the average of the scores, the function
# returns
#   * An "A" for an average greater than or equal to 90
#   * A "B" for an average greater than or equal to 80
#     and less than 90
#   * A "C" for an average greater than or equal to 70
#     and less than 80
#   * A "D" for an average greater than or equal to 60
#     and less than 70
#   * An "F" for any other average

# values is a list of scores
# loop over the values list and add each number
# create a variable of 0 that is the sum of the numbers in the list
# create an average variable that is the sum of numbers divided by list length
# create a series of if statements that show the grade


def calculate_grade(values):
    sum = 0

    for scores in values:
        sum += scores
    avg = sum / len(values)

    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


print(calculate_grade([100, 90, 80]))
print(calculate_grade([80, 90]))
print(calculate_grade([70, 80]))
print(calculate_grade([60, 70]))
print(calculate_grade([55, 60, 50]))
