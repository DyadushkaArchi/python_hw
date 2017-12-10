import math


#TEST 1
#
#

#task 1
a = 1
b = 2
c = 3
result = (a + b * c)**2
print(result)

#
#task 2
a = 1
b = 2
c = 3

if c == 0:
    print('Error: division by zero')
else:
    result = a - 4 * b / c
    print(result)

#
#task 3
a = 1
b = 2
c = 0

if c == 1:
    print('Error: division by zero')
else:
    result = (a * b + 4) / (c - 1)
    print(result)

#
#task 4

int_user_number = input("Введи пятизначное число: ")

if int_user_number.isnumeric() and 0 < int(int(int_user_number) / 10000) < 10:
    int_user_number = int(int_user_number)


    number5 = int_user_number % 10
    number4 = int((int_user_number % 100) / 10)
    number3 = int(int(int_user_number / 100) % 10)
    number2 = math.fmod(int(int_user_number / 1000), 10)
    number1 = int(int_user_number / 10000)

    if math.fmod(number5, 2) != 0:
        number5_is_not_even = number5
    else:
        number5_is_not_even = 1


    if math.fmod(number4, 2) != 0:
        number4_is_not_even = number4
    else:
        number4_is_not_even = 1

    if math.fmod(number3, 2) != 0:
        number3_is_not_even = number3
    else:
        number3_is_not_even = 1

    if (number2 % 2) != 0:
        number2_is_not_even = number2
    else:
        number2_is_not_even = 1

    if math.fmod(number1, 2) != 0:
        number1_is_not_even = number1
    else:
        number1_is_not_even = 1

    product_of_not_even_numbers = number5_is_not_even * number4_is_not_even * number3_is_not_even * number2_is_not_even * number1_is_not_even
    print("Произведение нечётных цифр твоего числа равнo:", product_of_not_even_numbers)
else:
    print("Введи ПЯТИЗНАЧНОЕ ЧИСЛО!!!")





#
# task 5

def near_number_10():
    user_choice = input('Input number:')

    user_choice = str(user_choice)
    user_choice = user_choice.split(',')
    user_choice1 = user_choice[0]
    user_choice2 = user_choice[1]

    if abs(10 - int(user_choice1)) < abs(10 - int(user_choice2)):
        return user_choice1
    else:
        return user_choice2




#
# task 6
def is_isogramm(text):
    for i in range(len(str(text))):
        current_letter = text[i-1]

        if text[i] == current_letter:
            return False
        else:
            return True


#
# task 9
def norm_list(lst):
    current_max = abs(lst[0])
    for i in range(len(lst)):

        if abs(lst[i-1]) > current_max:
            current_max = abs(lst[i-1])

    for i in range(len(lst)):
        lst[i-1] = lst[i-1] / current_max













