"""
generators
iterators
iterables
"""
import sys
import time

# l1 = [0,1,2,3,4,5]
# l1 = iter(l1)

# print(next(l1))


# print(hasattr(l1, '__next__'))

# l1 = list(range(10))
# print(sys.getsizeof(l1))

# def generate():
# 	for n in range(100):
# 		yield (n)
# 		time.sleep(0.1)

# g = generate()

# print(hasattr(g, '__iter__'))
# print(hasattr(g, '__next__'))

# def generate():
# 	variable = 'value 1'
# 	yield variable

# 	variable = 'value 2'
# 	yield variable


# 	variable = 'value 3'
# 	yield variable


# g = generate()

# for v in g:
# 	print(v)

# print(next(g))
# print(next(g))
# print(next(g))

l1 = [x for x in range(1000)]
print(type(l1))
l2 = (x for x in range(1000))
print(type(l2))

print(sys.getsizeof(l1))
print(sys.getsizeof(l2))