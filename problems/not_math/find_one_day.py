def skating_day_message(month_num, day_num):
    if month_num < 12:
        day = 1

    if month_num == 12 and day_num < 4:
        day = 1

    if month_num == 12 and day_num == 4:
        day = 2

    if month_num == 12 and day_num > 4:
        day = 3

    if day == 1:
        return "World Ice Skating Day is coming up!"
    if day == 2:
        return "YAY! It's World Ice Skating Day!"
    if day == 3:
        return "You just missed it. There's another next year!"
