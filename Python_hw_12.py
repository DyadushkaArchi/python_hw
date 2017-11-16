import math

#============================================================================
#task 12

#Написать функцию, которая рассчитывает сумму всех цифр некоторого трехзначного числа,
#введенного пользователем в консоли, без использования операторов цикла.
#Реализовать задачу без использования строк.

def amount(number):
    action1 = number / 100
    result1 = int(action1)

    action2 = math.fmod(number, 100)
    action2_1 = action2 / 10
    result2 = int(action2_1)

    action3 = math.fmod(number, 10)
    result3 = action3

    total_result = result1 + result2 + result3
    return total_result

example = amount(244)
print(int(example))

