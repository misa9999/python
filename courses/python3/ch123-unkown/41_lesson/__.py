# find all numbers from 1-1000 that are divisible by 7
lc1 = [number for number in range(1, 1001) if number % 7 == 0]

# find all numbers from 1-1000 that have a 3 in them
lc2 = [number for number in range(1, 1001) if '3' in str(number)]
# lc2 = [number for number in range(1, 1001) if [div for div in range(2, 10) if number % div == 0]]

# count the number of spaces in a string
string = 'I love python'

lc3 = [space for space in string if space == ' ']
# print(len(lc3))

# remove all of the vowels in a string
string1 = 'Look at the sky tonight'

lc4 = [vowel for vowel in string1 if not vowel in 'aeiou']

# print(''.join(lc4))

# find all of the words in a string that are less than 4 letters
# words = 'I love Python'
words = 'find all of the words in a string that are less than 4 letters'

lc5 = [word for word in words.split() if len(word) <= 4]
# print(lc5)

# use a dictionary comprehension to count the length of each word in a sentence
# use a nested list comprehension to find all of the numbers from  1-1000 that are divisible by any single digit besides 1 (2-9)
# for all the numbers 1-1000 use a nested list/dictionary comprehension to find the highest single digit any of the numbers is divisible by
