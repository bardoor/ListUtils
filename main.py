def del_doubles(lst: list) -> list:
    has_already = False
    for i in range(len(lst)):
        for j in range(len(lst)):
            if has_already == True and lst[j] == lst[i]:
                del lst[j]
                continue
            if lst[j] == lst[i]:
                has_already = True
        has_already = False
    return lst