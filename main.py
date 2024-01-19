<<<<<<< HEAD
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
=======
def del_doubles(lst: list) -> list:
    already_checked = []
    indexes_to_delete = []
    first_this = False
    for i in range(len(lst)):
        for j in range(len(lst)):
            if not(lst[i] in already_checked):
                if first_this == False and lst[i] == lst[j]:
                    first_this = True
                elif lst[i] == lst[j]:
                    indexes_to_delete.append(j)
        already_checked.append(lst[i])
        first_this = False

    itterations = 0
    for i in range(len(indexes_to_delete)):
        for j in range(len(indexes_to_delete) - itterations):
            if indexes_to_delete[i] > indexes_to_delete[j + itterations]:
                indexes_to_delete[i], indexes_to_delete[j + itterations] = indexes_to_delete[j + itterations], indexes_to_delete[i]
        itterations += 1

    index_smestitel = 0
    for i in indexes_to_delete:
        del lst[i - index_smestitel]
        index_smestitel += 1
    return lst


>>>>>>> 77523b6c5df880dbefd908dd5e021fd02f433e88
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
