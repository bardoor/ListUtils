from random import randint


def random_lst(n: int, from_num: int, to_num: int) -> list:
    lst = []
    
    for i in range(n):
        lst.append(randint(from_num,to_num))
    return lst

