from random import randint

soma = 0
while True:
    jogador = int(input('Jogue um número de 1 a 10: '))
    computador = randint(1, 10)

    escolha = input('Par ou Ímpar? [P/I]: ').upper()
    while escolha not in 'PI':
        print('Opção inválida! digite apenas P ou I')
        escolha = input('Par ou Ímpar [P/I]').upper()
    
    soma = jogador + computador
    par = soma % 2 == 0

    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} é {'par' if par else 'Ímpar'}')

    venceu = (escolha == 'P' and par) or (escolha == 'I' and not par)
    if venceu:
        print('Você venceu!')
    else:
        print('Você perdeu!')
        break
