"""ITERTOOLS
combinations
permutations
product
"""
from itertools import combinations, permutations, product


peoples = ['misa', 'yui', 'asuna', 'kira', 'kirito', 'megumin']

for group in product(peoples, repeat=2):
	print(group)

# for group in permutations(peoples, 2):
# 	print(group)

# for group in combinations(peoples, 2):
# 	print(group)