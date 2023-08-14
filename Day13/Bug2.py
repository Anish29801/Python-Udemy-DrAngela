import random
import time

def Buy2():
    dice = [1,2,3,4,5,6]
    dice_num  = dice[random.randint(0,5)] # random.randint(1,6)
    print(dice_num)
    
for i in range(1,11):
    Buy2()
    time.sleep(2)