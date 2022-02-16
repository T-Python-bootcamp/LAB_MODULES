import datetime


def check_day(y, m, d):
    d = datetime.datetime(y, m, d).strftime("%A")
    if d == "Thursday":
        return "True"
    else:
        return "False"
