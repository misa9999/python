try:
	a = 0
	try:
		a = 1/0
	except:
		print('error')
except NameError as e:
	print('NameError:', e)
except (IndexError, KeyError) as e:
	print('IndexError or KeyError')
except Exception as e:
	print('Unexpected error: ', e)
else:
	# print('[+] success')
	pass
finally:
	# print('finally')
	a = ''

print(a)