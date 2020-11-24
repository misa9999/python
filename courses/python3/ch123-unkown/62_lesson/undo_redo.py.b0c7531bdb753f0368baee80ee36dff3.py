from time import sleep


tasks = []
removed = []


def run():
	while True:
		menu()
		try:
			opt = int(input('[+] Choose an option: '))
			print()
			if opt == 1:
				add_task()
			elif opt == 2:
				list_tasks()
			elif opt == 3:
				undo()
			elif opt == 4:
				redo()
			elif opt == 5:
				break
			else:
				print('[!!] error, invalid option. Try again!')
		except Exception:
			print('[!!] Just Numbers')


def menu():
	print('-'*30)
	print('[1] add task')
	print('[2] list tasks')
	print('[3] undo')
	print('[4] redo')
	print('[5] exit')
	print('-'*30)
	print()


def add_task():
	task = input('[+] Add New Tasks: ')
	print()
	tasks.append(task)


def list_tasks():
	print('[-] TASKS:')
	print()
	if not tasks:
		print('[!] Empty Task List')
	for task in tasks:
		print('\t', task, flush=True)
		sleep(0.45)
	print()


def undo():
	try:
		removed.append(tasks.pop())
	except IndexError:
		print('[!!] Empty List')


def redo():
	try:
		tasks.append(removed.pop())
	except IndexError:
		print('[!!] Empty List')


if __name__ == '__main__':
	run()
