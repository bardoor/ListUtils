def find_element(lst,target):
    for i in range(len(lst)):       
        if lst[i] == target:
            index = i  
            break  
    return index
