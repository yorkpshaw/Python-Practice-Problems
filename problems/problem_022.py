# Complete the gear_for_day function which returns a list of
# gear needed for the day given certain criteria.
#   * If the day is not sunny and it is a workday, the list
#     needs to contain "umbrella"
#   * If it is a workday, the list needs to contain "laptop"
#   * If it is not a workday, the list needs to contain
#     "surfboard"

# Create an empty to list to append to
# If it is not sunny and it is a workday, return umbrella
# If it is a workday, return laptop
# If it is not a workday, return surfboard


def gear_for_day(is_workday, is_sunny):
    lst = []
    if is_workday and not is_sunny:
        lst.append("umbrella")
    if is_workday:
        lst.append("laptop")
    else:
        lst.append("surfboard")

    return lst


print(gear_for_day(True, True))
print(gear_for_day(False, False))
print(gear_for_day(False, True))
print(gear_for_day(True, False))
