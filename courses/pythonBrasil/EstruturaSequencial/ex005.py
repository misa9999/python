# converte metros para centimetros
n = float(input('Informe a medida: '))

km = n*0.001
hm = n*0.01
dm = n*10
cm = n*100
mm = n*1000
dam = n*0.1

print(f'''A medida de {n}m corresponde a
{km}→KM
{hm}→ HM
{dam}→DAM
{dm}→DM
{cm}→CM
{mm}→MM
''')
