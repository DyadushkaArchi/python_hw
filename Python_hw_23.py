import random

# task 23

number = random.randint(1, 10)
print('Hello! I came up with a number from 1 to 10. Try to guess!')

while True:
    user_choice = input('Write your number:')

    if int(user_choice) == number:
        print("Exellent!")
        break

    elif int(user_choice) > number:
        print('My number is less(')

    elif int(user_choice) < number:
        print('My number is more(')


