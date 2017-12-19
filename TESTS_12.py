import random

user_choice = input('Hello teacher! Click ENTER to start: ')

exercises = []
if user_choice == '':
    while len(exercises) < 36:
        rand_number1 = random.randint(2, 9)
        rand_number2 = random.randint(2, 9)
        example1 = '%d * %d' % (rand_number1, rand_number2)
        example2 = '%d * %d' % (rand_number2, rand_number1)
        if not example1 in exercises and example2 not in exercises:
            exercises.append(example1)

    result = []

    while len(result) < 15:
        rand_example = exercises[random.randint(0, 30)]
        if not rand_example in result:
            result.append(rand_example)

    for i in range(len(result)):
        print(result[i])

