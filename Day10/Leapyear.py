
def leapyearOrNot(year):
    year = int(year)
    if (year%4 == 0):
        res = True
    else:
        res = False
    return res

print(leapyearOrNot(2024))


def daysinmonths(month,year):
    if(leapyearOrNot(year) == True and month == 2):
        res = 29
    elif(leapyearOrNot(year) == False and month == 2):
        res = 28
    elif(month%2 != 0):
        res = 31
    else:
        res = 30