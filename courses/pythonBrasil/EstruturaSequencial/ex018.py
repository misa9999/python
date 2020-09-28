# pede o tamanho do arquivo em MB e a velocidade da net em mbps e informa o tempo aproximado de down em min

# tamanho do arquivo
tamanho = int(input('Informe o tamanho do arquivo em MB: '))

# velocidade da internet
net_vel = float(input('Informe a velocidade da net em mbps: '))

# divide o tamanho pela velo/sec e obtem os segundos aproximados
t = tamanho / net_vel

# converte os segundos para minutos
min = t / 60

# checa se o download é menor ou maior que 60 segundos
if t < 60:
    print(f'tempo aproximado {int(t)} segundos')
else:
    print(f'Tempo aproximado {int(min)} minuto(s)')
