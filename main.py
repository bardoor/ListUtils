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

