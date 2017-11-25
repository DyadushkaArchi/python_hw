import random

def find_min_max_diff(num_limit, lower_bound, upper_bound):

    current_max = lower_bound
    for i in range(num_limit):

        rand_number = random.randint(lower_bound, upper_bound)
        print('rand.number: ', rand_number)

        if rand_number > current_max:
            current_max = rand_number


    current_min = upper_bound
    for i in range(num_limit):

        rand_number = random.randint(lower_bound, upper_bound)
        print('rand.number: ', rand_number)

        if rand_number < current_min:
            current_min = rand_number


    result = current_max - current_min
    return result

result = find_min_max_diff(10, 100, 200)
print("Diff between max and min: %d" % result)