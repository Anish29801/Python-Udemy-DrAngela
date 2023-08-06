import math

def AvgHeights(list):
    avg = 0
    for i in range(len(list)):
        avg += list[i]/len(list)
    return math.floor(avg)

list = [ 180,124,165,173,189,169,146 ]
print(AvgHeights(list))