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


