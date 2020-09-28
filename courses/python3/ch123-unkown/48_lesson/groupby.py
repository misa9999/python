from itertools import groupby, tee

students = [
	{'name': 'Misa', 'note': 'A'},
	{'name': 'Megumin', 'note': 'B'},
	{'name': 'Yuuki', 'note': 'A'},
	{'name': 'Mira', 'note': 'A'},
	{'name': 'Aqua', 'note': 'C'},
	{'name': 'Yui', 'note': 'B'},
	{'name': 'Yukinoshita', 'note': 'A'},
	{'name': 'Nami', 'note': 'A'},
	{'name': 'Robin', 'note': 'B'},
	{'name': 'Karen', 'note': 'C'},
]


sort_items = lambda item: item['note']
students.sort(key=sort_items)
students_group = groupby(students, sort_items)

for note, value in students_group:
	va1, va2 = tee(value)

	print(f'Note: {note}')

	for student in va1:
		print(f'\t{student}')

	tot = len(list(va2))
	print(f'\t{tot} students with note: {note}')
	print()