import random


def get_max_digit():  # returns int
    number = random.randint(1000000000, 1000000000000)
    print(number)
    current_max = number % 10

    for i in range(len(str(number))):
        part_of_number = number % 10
        if part_of_number > current_max:
            current_max = part_of_number
        number = int(number / 10)

    return current_max

print(get_max_digit())