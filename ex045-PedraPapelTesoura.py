# Crie um programa que faça o computador jogar Jokenpô com você!

from random import choice

jogador = input('Escolha entre Pedra, Papel e Tesoura: ').capitalize()
computador = choice(['Papel', 'Pedra', 'Tesoura'])

print('Valendo...')
print(f'Computador: {computador}\nJogador: {jogador}')

if (computador == 'Papel' and jogador == 'Pedra') or \
    (computador == 'Pedra' and jogador == 'Tesoura') or \
    (computador == 'Tesoura' and jogador == 'Papel'):
    print('Eu ganhei!')
    
elif computador == jogador:
    print('Empate!')

elif jogador in ['Papel', 'Tesoura', 'Pedra']:
    print('Você ganhou!')
    
else:
    print('Jogue direito, digite Pedra, Papel ou Tesoura!')