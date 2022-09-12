# Complete the gear_for_day function which returns a list of
# gear needed for the day given certain criteria.
#   * If the day is not sunny and it is a workday, the list
#     needs to contain "umbrella"
#   * If it is a workday, the list needs to contain "laptop"
#   * If it is not a workday, the list needs to contain
#     "surfboard"


def gear_for_day(is_workday, is_sunny):
    workday_list = []
    if is_workday and not is_sunny:
        workday_list.append("umbrella")
    elif is_workday:
        workday_list.append("laptop")
    else:
        workday_list.append("surfboard")

    return workday_list


print(gear_for_day(True, False))
print(gear_for_day(True, True))
print(gear_for_day(False, True))
