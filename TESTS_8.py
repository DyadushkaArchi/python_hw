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

sum = current_min + current_max
lst[index_max] = sum - current_max
lst[index_min] = sum - current_min
print(lst)




