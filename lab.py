import datetime

def isThur(year:int, month:int, day:int):
    x = datetime.datetime(year, month, day)
    if x.strftime("%A") == "Thursday":
        print("True")
    else:
        print("False") 

isThur(2022, 2, 17)
isThur(2022, 2, 16)