def find_element(lst,target):
    index = -1
    for i in range(len(lst)):
        if lst[i] == target:
            index = i  
    return index

