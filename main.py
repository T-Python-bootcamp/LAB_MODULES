
import datetime

while True:
    str=input('Enter Date in the following format: yyyy mm dd: ').split(' ')
    print(datetime.datetime(int(str[0]),int(str[1]),int(str[2])).strftime("%A")=='Thursday')
