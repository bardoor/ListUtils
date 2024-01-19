def gtr_inique_lst(lst):
    unique = []
    for number in lst:
        if number in unique:
            continue
        else:
            unique.append(number)
    return unique