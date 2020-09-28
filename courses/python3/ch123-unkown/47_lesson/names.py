from itertools import permutations


first_name = input('[*] Enter First Name: ')
last_name = input('[*] Enter Last Name: ')
fav_color = input('[*] Enter Favorite color: ')
dog_name = input('[*] Enter Dog Name: ')
boyfriend_name = input('[*] Enter Boyfriend Name: ')
fav_team = input('[*] Enter Favorite Team: ')
s1 = '-'
s2 = '_'


for name in permutations((first_name, last_name, fav_color,
						  dog_name, boyfriend_name, s1, s2), 2):
	print(name)