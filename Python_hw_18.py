#==============================================================================
#task 18
#==============================================================================
#Каждому символу в таблице символов Unicode соответствует число.
#Написать функцию, которая рассчитывает сумму чисел,
#которые соответствуют символам, стоящим между двумя заданными включительно.
#Например, в функцию передаются символы ‘x’ и ‘z’.
#Значит надо вычислить сумму кодов символов ‘x’,’y’,’z’.

def sum_symbol_codes(first, last): # returns int
    first_code = int(ord(str(first)))
    last_code = int(ord(str(last)))

    total_sum = 0
    for i in range(first_code, last_code + 1):
        total_sum += i
    return total_sum


print(sum_symbol_codes('x', 'z'))
















