l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [1, 2, 3, 4]

# result = [x[0] + x[1] for x, y in zip(l1, l2)]
result = [x + y for x, y in zip(l1, l2)]
print(result)

# generic
# l3 = []
# for i in range(len(l2)):
# 	l3.append(l1[i] + l2[i])

# print(l3)

# for i, _ enumerate(range(l2)):
# 	l3.append(l1[i] + l2[i])
