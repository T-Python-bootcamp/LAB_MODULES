import calendar

def checkDay(year:int, month:int, day:int):
    if calendar.weekday(year, month, day) == 3:
        return True
    else:
        return False