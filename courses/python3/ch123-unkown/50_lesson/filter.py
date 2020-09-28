from data import products, peoples, l1


# new_list = filter(lambda x: x > 5, l1)
# new_list = [x for x in l1 if x > 5]

# def filter_(product):
# 	if product['price'] > 50:
# 		return True
# 	return False

def filter_(people):
	if people['age'] >= 18:
		return True
	return False

# new_list = filter(lambda p: p['price'] > 50, products)
new_list = filter(filter_, peoples)

for people in new_list:
	print(people)