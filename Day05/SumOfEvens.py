def SumOfEvens():
    sum = 0
    for i in range(101):
        if(i%2 == 0):
            sum += i
    return sum

print(SumOfEvens())

