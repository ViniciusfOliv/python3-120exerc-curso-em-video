p_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = p_termo
cont = 1
total = 0
mais_termos = 10

while mais_termos != 0:
    total = total + mais_termos
    while cont <= total:
        print(f'{termo}', end=' ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais_termos = int(input('Digite mais termos para ver ou [0] para sair: '))
print('FIM')