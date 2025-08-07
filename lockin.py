def add_two_lists():
    list1 = list(map(int, input("Enter list 1: ").split()))
    list2 = list(map(int, input("Enter list 2: ").split()))
    
    result = []
    
    for i in range(len(list1)):
        result.append(list1[i] + list2[i])
        
    return result

print(add_two_lists())


