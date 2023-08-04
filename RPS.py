list = ['rock', 'paper','scissors']


if(val == 0 and cmpval == 1):
    flag = -1
elif(val == 0 and cmpval == 2 ):
    flag = 1
elif(val == 1 and cmpval == 2):
    flag = -1
elif(val == 1 and cmpval == 0 ):
    flag = 1
elif(val == 2 and cmpval == 1):
    flag = 1
elif(val == 2 and cmpval == 0):
    flag = -1
else:
    flag = 0