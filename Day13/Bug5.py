

def mutate(a_list):
    b_list = []
    for i in range(len(a_list)):
        newItem = a_list[i] * 2
        b_list.append(newItem)
    print(b_list)
    
    
mutate([1,3,5,8,13])