# Crie um programa que leia dois valroes e msotre um menu na tela:
# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos números
# [5] Sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
escolha = 0

while escolha != 5:
    print('\nMenu:\n' \
    '[1] Somar\n'
    '[2] Multiplicar\n' \
    '[3] Maior número\n'
    '[4] Novos números\n'
    '[5] Sair do programa\n')

    escolha = int(input('Dígite o número da opção desejada: '))

    if escolha == 1:
        print(f'A soma dos valores é {n1 + n2}')
    elif escolha == 2:
        print(f'A multiplicação dos valores é {n1 * n2}')
    elif escolha == 3:
        if n1 > n2:
            print(f'O maior valor é {n1}')
        elif n2 > n1:
            print(f'O maior valor é {n2}')
        else:
            print(f'Os valores são iguais. {n1} - {n2}')
    elif escolha == 4:
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo valor: '))
    elif escolha == 5:
        print('Finalizando...')
    else:
        print('Opção inválida, tente novamente!')
    
print('Você saiu do programa.')