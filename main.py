<<<<<<< HEAD
def gen_posled():
    lst = []
    n = input("Введите начало последовательности>>")
    m = input("Введите конец последовательности>>")
    k = input("Введите шаг>>")
    if n.isdigit() and m.isdigit() and k.isdigit() and m>n and m > k:
        n = int(n)
        m = int(m)
        k = int(k)
        for i in range(n,m,k):
            lst.append(i)
        return lst
    else:
        print("Вы ввели неверное значение")


=======
def gtr_inique_lst(lst):
    unique = []
    for number in lst:
        if number in unique:
            continue
        else:
            unique.append(number)
    return unique
from random import randint


def random_lst(num: int, from_num: int, to_num: int) -> list:
    lst = []
    if type(num) != int:
        raise ValueError("Вы ввели не целое число")
    elif type(from_num) != int:
        raise ValueError("Вы ввели не целое число")
    elif type(to_num) != int:
        raise ValueError("Вы ввели не целое число")
    else:
        for i in range(num):
            lst.append(randint(from_num,to_num))
        return lst


def find_element(lst,target):
    index = -1
    for i in range(len(lst)):
        if lst[i] == target:
            index = i  
    return index


def poisk_chs(lst):
    dup = []
    for i in lst:
        if lst.count(i) > 1 and i not in dup:
            dup.append(i)
    return dup
>>>>>>> 1a361454c5cf505c6dd8f2cdaeee4db07c03f963
