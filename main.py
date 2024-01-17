lst = [1132,22342,3453,4235]
target = int(input())
def find_element(lst,target):
    index = -1
    for i in range(len(lst)):
        if lst[i] == target:
            index = i  
    return index
print(find_element(lst,target))
