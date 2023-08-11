    
def calc(num1, num2,oper):
    result = 0
    match oper:
        case '+': 
            result = num1 + num2
        case '-': 
            result = num1 - num2
        case '*': 
            result = num1 * num2
        case '/': 
            result = num1 / num2
        case '%': 
            result = num1 % num2
        case _:
            result = 0
    return result

def menu():
    print("+")
    print("-")
    print("*")
    print("/")
    oper = input("Enter the operation you are interested in? ")
    if(oper == '+' or 
       oper == '-'or
       oper == '*'
       or oper== '/'):
        num1 = int(input("Enter a number : "))
        num2 = int(input("Enter a number : "))
        res = calc(num1, num2,oper)
        print (res)
    else:
        print("Invalid operator Entered")
    
while True:
    menu()
    choice= input("Enter your choice Y/N: ")
    choice = choice.lower()
    if(choice == 'n'):
        break