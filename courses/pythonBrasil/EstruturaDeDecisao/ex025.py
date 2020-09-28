'''
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a
 participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela
 deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5
 como "Assassino". Caso contrário, ele será classificado como "Inocente"
'''

posi = 0
estado = ""


def checar(resp):
    global posi
    if resp in 'sS':
        posi += 1
    elif resp in 'nN':
        ...
        

p1 = input('Telefonou para a vitima? (S/N) ').strip().lower()[0]
p2 = input('Esteve no local do crime? (S/N) ').strip().lower()[0]
p3 = input('Mora perto da vítima? (S/N) ').strip().lower()[0]
p4 = input('Devia para a vítima? (S/N) ').strip().lower()[0]
p5 = input('Já trabalhou com a vítima? (S/N) ').strip().lower()[0]

perg = [p1, p2, p3, p4, p5]
for x in perg:
    checar(x)


if posi == 0 or posi == 1:
    estado = "Inocente"
elif posi == 2:
    estado = "Suspeita"
elif posi == 3 or posi == 4:
    estado = "Cúmplice"
elif posi == 5:
    estado = "Assassino"
else:
    print('Opção invalida')


print(f'Você é considerado "{estado}" no crime.')
