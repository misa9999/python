# import sales.calc_prices
# from sales import calc_prices
from sales.calc_prices import increase, reduction
# from sales.format.price import dollar


price = 49.90
# increase_price = sales.calc_prices.increase(value=price, percentage=15)
# increase_price = calc_prices.increase(value=price, percentage=15)

increase_price = increase(value=price, percentage=15, format=True)
print(increase_price)

reduction_price = reduction(value=price, percentage=15, format=True)
print(reduction_price)