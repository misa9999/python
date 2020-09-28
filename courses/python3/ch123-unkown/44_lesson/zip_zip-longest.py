"""
Zip
Zip_longest - Itertools
"""

from itertools import zip_longest, count

index = count()
cities = ['Tokyo', 'Delhi', 'Shanghai', 'São Paulo', 'Mexico City', 'Cairo']
countries = ['Japan', 'India', 'China', 'Brasil', 'Mexico', 'Egypt']

cities_countries = zip(
    index,
    cities, 
    countries
)

for index, country, city in cities_countries:
	print(index, country, city)

#print(next(citites_countries))
#for value in cities_countries:
    #print(value)
