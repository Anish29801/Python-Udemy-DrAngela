import math
class TipSpliter:
    # Create a constructor
    def __init__(self):
        print("Welcome to Tip Spliter.")
    def Spliter(bill,people,tipPercent):
         val = bill/people
         val+= (val * tipPercent)/100
         return math.ceil(val)
    

obj = TipSpliter
bill = float(input('Enter your bill $'))
people = int(input('Enter number of people'))
tipPercent = float(input(' Enter percentage of tip'))
print(obj.Spliter(bill, people, tipPercent)) 
    