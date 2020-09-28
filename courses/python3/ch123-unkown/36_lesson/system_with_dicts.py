questions = {
	'Question 1': {
		'question': 'How much is 2 + 2? ',
		'answers': {
			'a': '1',
			'b': '4',
			'c': '5',
		},
		'right answer': 'b',
	},
	'Question 2': {
		'question': 'How much is 3 * 2? ',
		'answers': {
			'a': '4',
			'b': '10',
			'c': '6',
		},
		'right answer': 'c',
	},
	'Question 3': {
		'question': 'How much is 8 + 2? ',
		'answers': {
			'a': '10',
			'b': '4',
			'c': '5',
		},
		'right answer': 'a',
	},
	'Question 4': {
		'question': 'How much is 8 + 2? ',
		'answers': {
			'a': '1',
			'b': '16',
			'c': '5',
		},
		'right answer': 'b',
	},
	'Question 5': {
		'question': 'How much is 9 - 4? ',
		'answers': {
			'a': '1',
			'b': '4',
			'c': '5',
		},
		'right answer': 'c',
	},
}

print()

right_answers = 0
for qk, qv in questions.items():
	print(f'{qk}: {qv["question"]}')

	# print('\nPlease choose one of the options below.\n')
	print('Answers:')
	for ak, av in qv['answers'].items():
		print(f'[ {ak} ]: {av}')

	user_answer = input('Your answer: ')

	if user_answer == qv['right answer']:
		print("YEAAAAAHHHH!! You're right!!!")
		right_answers += 1
	else:
		print("DAMN IT!!!! you missed!!!")

	print()

number_of_questions = len(questions)
percentage_of_answers_correct = right_answers / number_of_questions * 100

print(f"You're right {right_answers} answers.")
print(f"Your hit percentage was {percentage_of_answers_correct }%")