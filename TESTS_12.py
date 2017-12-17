import random

user_choice = input('Hello teacher! Click ENTER to start: ')

exercises = []
if user_choice == '':
    while len(exercises) < 36:
        example = '%d * %d' % (random.randint(2, 9), random.randint(2, 9))
        if not example in exercises:
            exercises.append(example)

    result = []

    while len(result) < 15:
        rand_example = exercises[random.randint(0, 30)]
        if not rand_example in result:
            result.append(rand_example)

    for i in range(len(result)):
        print(result[i])

