import datetime

def checkDay (date):
    date = date.split("/")
    day, month, year = (int(date[0]),int(date[1]),int(date[2]))
    # print(day,month,year)
    intDay = datetime.date(year, month, day).weekday()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if days[intDay] == "Thursday":
        return True
    else:
        return False

print(checkDay("5/02/2022"))