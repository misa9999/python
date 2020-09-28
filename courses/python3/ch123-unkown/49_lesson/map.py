from data import products, peoples, l1


def plus_age(p):
	p['new_age'] = round(p['age'] * 1.20)
	return p

# names = map(lambda p: p['name'], peoples)
names = map(plus_age, peoples)

for people in names:
	print(people)

# names2 = [x['name'] for x in peoples]
# print('\n'.join(names2))
# print()


# def price_plus(p):
# 	p['price'] = round(p['price'] * 1.05, 2)
# 	return p


# prices = map(lambda p: p['price'], products)
# prices = map(price_plus, products)

# for price in prices:
# 	print(price)

# new_list = list(map(lambda x: x*2, l1))
# new_list = [x*2 for x in l1]
# print(new_list)