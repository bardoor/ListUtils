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