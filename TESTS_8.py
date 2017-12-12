# В одномерном списке поменять местами минимальный и максимальный элементы.
# Остальные оставить на своих местах.

lst = [1, 2, 3]
current_max = lst[0]
current_min = lst[0]
for i in range(len(lst)):

    if lst[i] > current_max:
        current_max = lst[i]
        index_max = i
    else:
        current_min = lst[i]
        index_min = i

lst[index_max] = current_min
lst[index_min] = current_max

print(lst)




