import datetime
def isThursday(y,m,d):
    day=datetime.date(y,m,d)
    if day.weekday()==3:
        return True
    else:
        return False   
print(isThursday(1999,10,7))
    