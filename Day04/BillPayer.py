import random

NoOfPeople = int(input('Enter the number of people : '))
BillPayer = random.randint(1, NoOfPeople)

print('Member '+str(BillPayer) +' shall pay the bill')