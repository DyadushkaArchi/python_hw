# Создайте список из 11 случайных целых чисел из отрезка [-1;1].
# Передайте его в функцию, которая определит какой элемент встречается в списке чаще всего и вернет этот элемент.
# Однако, если два каких-то элемента встречаются одинаковое количество раз,
# то вернуть None, а не самый часто встречающийся элемент.

lst = [-1, 0, 1, 1, -1, 0, 1, -1, -1, 0, 0]


def calc_frequency(lst):  # returns the most frequent number or None

    lst1 = []
    lst2 = []
    lst3 = []

    for i in range(len(lst)):
        if lst[i - 1] == -1:
            lst1 += [1]
        elif lst[i - 1] == 0:
            lst2 += [1]
        elif lst[i - 1] == 1:
            lst3 += [1]

    if len(lst1) > len(lst2) and len(lst1) > len(lst3):
        return -1
    elif len(lst2) > len(lst1) and len(lst3):
        return 0
    elif len(lst3) > len(lst1) and len(lst2):
        return 1
    else:
        return None


print(calc_frequency(lst))