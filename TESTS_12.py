import random

user_choice = input('Hello teacher! Click ENTER to start: ')
examples = ['2*2', '2*3', '2*4', '2*5', '2*6', '2*7', '2*8', '2*9', '3*3', '3*4', '3*5', '3*6', '3*7', '3*8', '3*9',
            '4*4', '4*5', '4*6', '4*7', '4*8', '4*9', '5*5', '5*6', '5*7', '5*8', '5*9', '6*6', '6*7', '6*8', '6*9',
            '7*7', '7*8', '7*9', '8*8', '8*9', '9*9']
result = []

if user_choice == '':
    while len(result) < 15:
        rand_example = examples[random.randint(0, 30)]
        if not rand_example in result:
            result.append(rand_example)

    for i in range(len(result)):
        print(result[i])