p_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA:'))
inicio = p_termo
cont = 1
while cont <= 10:
    print(f'{p_termo}', end=' > ')
    p_termo += razao
    cont += 1
print('FIM')