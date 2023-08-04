import math

def BMICalculator(height,weight):
    return math.ceil(weight/height)
print('Welcome to BMI Calculator')
Myheight = float(input("Please enter your height in m "))
Myweight = float(input("Please enter your weight in kg "))

MyBmi = BMICalculator(Myheight, Myweight)
print("Your BMI : " + str(MyBmi))

def healthChecker(bmi):
    if (bmi < 18.5 ):
        print("You are underweight")
    elif (bmi >= 18.5 and bmi <24.9):
        print ("You are healthy")
    elif (bmi >= 24.9 and bmi < 29.4):
        print ("You are Overweight")
    else:
        print ("You are facing Obesity")