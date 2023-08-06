
power = True

def ElectrictyProblem(electricty,steps):
    i = 0
    bill = 0
    while (electricty and i < steps > 0):
        print("Moving "+str(i+1)+" steps")
        i+=1
        bill+=5
        if(i == (steps)):
            electricty = False
            print("No power! check connection")   
            
    if(bill == 0):
        print("Thank you for connecting!")
    return str(bill)
        
print ("Bill : $"+ ElectrictyProblem(power,0))