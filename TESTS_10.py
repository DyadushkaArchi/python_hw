# Для заданной матрицы (3*3) найти все ее седловые точки и вернуть список их координат (список списков).
# Седловых точек может не быть, может быть 1 и более.

def saddle_point(lst):
    current_max = lst[0]
    for i in range(3):
        if lst[i] > current_max:
            current_max = lst[i]

        current_min = lst[0]
        for j in range(3):
            if lst[j] < current_min:
                current_min = lst[j]

        if current_max == current_min:
            return ([i, j])


