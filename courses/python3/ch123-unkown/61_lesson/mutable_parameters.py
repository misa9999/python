# mutable: lists, dicts, etc...
# imutable: tuples, strings, numbers, True, False, None

def client_list(iterable_clients, list=None):
	if list is None:
		list = []
	list.extend(iterable_clients)
	return list

l1 = ['kira']
clients1 = client_list(['misa', 'lucy', 'yukinoshita'], l1)
clients2 = client_list(['yui', 'asuna', 'megumin'])
clients3 = client_list(['kirito'])

print(clients1)
print(clients2)
print(clients3)