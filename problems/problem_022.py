# Complete the gear_for_day function which returns a list of
# gear needed for the day given certain criteria.
#   * If the day is not sunny and it is a workday, the list
#     needs to contain "umbrella"
#   * If it is a workday, the list needs to contain "laptop"
#   * If it is not a workday, the list needs to contain
#     "surfboard"


def gear_for_day(is_workday, is_sunny):
    gear = []
    # define gear_for_day which returns a list of strings
    if is_sunny == False and is_workday == True:
        gear.append("umbrella")
    # if is_sunny == False and is_workday ==True
    # return gear_for_day.append("umbrella")
    if is_workday == True:
        gear.append("laptop")
    # if is_workday == True
    #   return gear_for_day.append("laptop")
    if is_workday == False:
        gear.append("surfboard")
    return gear
    # if is_workday == False
    #   return gear_for_day.append("surfboard")


print(gear_for_day(True, False))
print(gear_for_day(True, True))
print(gear_for_day(False, False))
# print(gear_for_day(True,False))
# print(gear_for_day(True, True))
# print(gear_for_day(False,False))
