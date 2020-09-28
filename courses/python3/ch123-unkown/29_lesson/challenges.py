""" DONE
def greetings(greeting, name): # challenge 01 - greetings
	print(greeting, name)

greetings('Hi', 'Misa')
greetings('Hello', 'Misa')
greetings('Ohayou', 'Misa')
greetings('Yahallo', 'Misa')
"""


""" DONE
def my_sum(n1, n2, n3): # challenge 02 - sum numbers
	return n1 + n2 + n3


nums = my_sum(5, 5, 10)
print(nums)
"""

"""
def percentage_increase(value, percentage): # challenge 03 - show percentage increase
	return value + (value * percentage / 100)

var = percentage_increase(60, 45)
var2 = percentage_increase(15, 100)
var3 = percentage_increase(10, 10)
print(var)
print(var2)
print(var3)
"""


""" DONE
def fizz_buzz(): # challenge 04 - fizz buzz
	for num in range(1, 51):

		last_digit = num % 10

		if (num % 3 == 0 and last_digit == 0) or (num % 3 == 0 and last_digit == 5):
			print(f'{num} - FizzBuzz')

		elif num % 3 == 0:
			print(f'{num} - FIZZ')

		elif last_digit == 0 or last_digit == 5:
			print(f'{num } - BUZZ')

num = fizz_buzz()
"""

def fb(num):
	if num % 3 == 0 and num % 5 == 0:
		return f'FizzBuzz - {num}'

	if num % 3 == 0:
		return f'Fizz - {num}'

	if num % 5 == 0:
		return f'Buzz - {num}'

	return num

from random import randint

for i in range(100):
	random_ = randint(1, 100)
	print(fb(random_))

