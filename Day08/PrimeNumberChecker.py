

def PrimeNumberChecker(number):
    counter = 0
    for i in range(1, number+1):
        if(number%i == 0):
            counter += 1
    if(counter == 2):
        flag = "Prime"
    else:
       flag = "Non Prime"
    
    return flag

num = int(input("Enter a number : "))
print("Number "+str(num)+" is " +str(PrimeNumberChecker(num)))