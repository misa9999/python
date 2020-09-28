"""
add # adds an element to the set
update # update the set with the union of this set and others
clear # remove all the elements from the set
discard # remove the specified item
union | # returns a new set with all items from both sets
intersection & # returns a set, that is the intersection of two others sets
difference - # returns a set containing the difference between two or more sets
symmetric_difference ^ # returns a set with the symmetric differences of two sets
"""

# s1 = {1, 2, 3, 4, 5, 6}
# print(s1)

# l1 = [1,2,3,4,5,6,6,6,6,7,7,8,1,2,3, 'lul', 'lul']
# print(l1)
# l1 = set(l1)
# l1 = list(l1)
# print(l1)

# s1 = {1, 2, 3, 4, 5, 7}
# s2 = {1, 2, 3, 4, 5, 6}
# # s3 = s1 | s2 # union
# # s3 = s1 & s2 # intersection
# # s3 = s1 - s2 # difference
# s3 = s1 ^ s2 

# print(s3)

l1 = ['misa', 'yui', 'asuna']
l2 = ['yui', 'asuna', 'misa', 'misa', 'misa', 'misa']

if set(l1) == set(l2):
	print('L1 == L2')
else:
	print('L1 != L2')


# l1 = list(set(l1))
# l2 = list(set(l2))

# print(l1, l2)

