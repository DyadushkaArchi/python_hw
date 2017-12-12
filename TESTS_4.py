import math

num = 1
int_user_number = input("Введи пятизначное число: ")

if int_user_number.isnumeric() and 0 < int(int(int_user_number) / 10000) < 10:
    while int(int_user_number) > 0:
        digit = int(int_user_number) % 10
        int_user_number = int(int(int_user_number) / 10)

        if digit % 2 != 0:
                num *= digit

else:
    print("Введи ПЯТИЗНАЧНОЕ ЧИСЛО!!!")

print(num)


