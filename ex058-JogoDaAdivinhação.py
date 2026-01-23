# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar. Mostrando no final quantos palpites foram necessários para vencer.

from random import randint

computador = randint(0, 10)
tentativas = 1
acertou = False

while not acertou:
    jogador = int(input('Escolha um número de 0 a 10: '))

    if jogador == computador:
        print('Você acertou!')
        acertou = True
    else: 
        if jogador < computador:
            print('Tente chutar mais alto...')
            tentativas += 1
        elif jogador > computador:
            print('Tente chutar mais baixo...')
            tentativas += 1

print(f'Você acertou o número com {tentativas} tentativas.')