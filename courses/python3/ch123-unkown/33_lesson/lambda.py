# a = lambda x, y: x*y
# print(a(2, 2))

list_ = [
	['P1', 13],
	['P2', 6],
	['P3', 7],
	['P4', 50],
	['P5', 8]
]

# def func(item):
# 	return item[1]

# list_.sort(key=lambda item: item[1])

print(sorted(list_, key=lambda item: item[1]))