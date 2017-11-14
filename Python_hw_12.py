import math

#============================================================================
#task 12

#Написать функцию, которая рассчитывает сумму всех цифр некоторого трехзначного числа,
#введенного пользователем в консоли, без использования операторов цикла.
#Реализовать задачу без использования строк.

def amount(xyz):
    action1 = xyz / 100
    result1 = int(action1)

    action2 = math.fmod(243, 100)
    action2_1 = action2 / 10
    result2 = int(action2_1)

    action3 = math.fmod(xyz, 10)
    result3 = action3

    total_result = result1 + result2 + result3
    return total_result

example = amount(243)
print(int(example))

