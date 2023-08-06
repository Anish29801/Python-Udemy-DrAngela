import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
number = str(number)
special = ['*', '+', '-', '?']
list = letters + number + special

    
lengthOfPwd = int(input("Please enter length of your password"))
password = ''

for i in range(lengthOfPwd):
    password += list[random.randint(0, lengthOfPwd)]


print (password)