import random

#==========================================================================
#task 19
#==========================================================================
#Написать функцию для поиска разницы сумм всех четных и всех нечетных чисел среди
#100 случайно сгенерированных чисел в произвольном числовом диапазоне.
#Т.е. от суммы четных чисел вычесть сумму нечетных чисел.

def diff_even_odd(num_limit, lower_bound, upper_bound): # returns int
	even_number = 0
	odd_number = 0
	for i in range(num_limit):
		rand_number = random.randint(lower_bound, upper_bound)
		print("Rand.number:", rand_number)

		if rand_number % 2 == 0:
			even_number += rand_number

		else:
			odd_number += rand_number

	result = even_number - odd_number
	return result


example = diff_even_odd(4, -20, 0)
print(example)




