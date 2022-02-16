import datetime

def check(year, month, day):

    x = datetime.datetime(year, month, day)
    if x.strftime("%A") == "Thursday":
        print("True")
    else:
        print("False")
        
check(2021, 12, 23)