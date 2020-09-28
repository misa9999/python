
cart = []

cart.append(('product 1', 30))
cart.append(('product 2', 20))
cart.append(('product 3', 50))
cart.append(('product 4', 50))
cart.append(('product 5', 50))
cart.append(('product 6', 50))

tot = sum([float(x) for y, x in cart])
print(f'Total: R${tot:.2f}')