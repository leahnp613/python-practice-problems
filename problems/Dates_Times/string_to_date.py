def make_a_date(values):
    from datetime import date

    year = int(values[0])
    month = int(values[1])
    day = int(values[2])
    new_date = date(year, month, day)
    return new_date
