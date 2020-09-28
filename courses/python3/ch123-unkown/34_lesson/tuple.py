"""
tuple - imutable
"""

# t1 = (1, 2, 'a', 'misa')
# t2 = 4, 5, 6
# t3 = t1 + t2

# n1, n2, n3, *_, n6 = t3

# print(n1, n2, n3, _, n6)
t1 = (1, 2, 3, 4, 5)

t1 = list(t1)
t1[1] = 3000
t1 = tuple(t1)

print(t1)
