# lê um número e exibe o dia correspondente da semana

# pede um número correspondente a semana
dia = int(input('''Digite um número da semana:
[ 1 ] - Domingo
[ 2 ] - Segunda-feira
[ 3 ] - Terça-feira
[ 4 ] - Quarta-feira
[ 5 ] - Quinta-feira
[ 6 ] - Sexta-feira
[ 7 ] - Sabado
>>> '''))

# compara e printa o dia correspondente ao número escolhido
if dia == 1:
    print('Domingo')
elif dia == 2:
    print('Segunda-feira')
elif dia == 3:
    print('Terça-feira')
elif dia == 4:
    print('Quarta-feira')
elif dia == 5:
    print('Quinta-feira')
elif dia == 6:
    print('Sexta-feira')
elif dia == 7:
    print('Sabado')
else:
    print('Opção inválida')
