
def callme():
    print("Calling a process")

while True:
    callme()
    choice= input("Enter your choice Y/N: ")
    choice = choice.lower()
    if(choice == 'n'):
        break