from data import products, peoples, l1
from functools import reduce


# sum_list = reduce(lambda ac, i: i + ac, l1, 0)
# sum_prices = reduce(lambda ac, p: p['price'] + ac, products, 0)
# print(sum_prices / len(products))

sum_age = reduce(lambda ac, p: ac + p['age'], peoples, 0)
print(sum_age / len(peoples))