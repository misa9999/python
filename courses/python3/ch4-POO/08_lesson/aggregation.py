class Cart:
    def __init__(self):
        self.products = []

    def insert_product(self, product):
        self.products.append(product)

    def show_products(self):
        for product in self.products:
            print(product.name, product.value)

    def sum_total(self):
        total = 0
        for product in self.products:
            total += product.value
        return total


class Product:
    def __init__(self, name, value):
        self.name = name
        self.value = value


cart = Cart()
p1 = Product('cookie', 10)
p2 = Product('cake', 20)
p3 = Product('ice cream', 5.70)
cart.insert_product(p1)
cart.insert_product(p2)
cart.insert_product(p3)
cart.show_products()
print(cart.sum_total())
