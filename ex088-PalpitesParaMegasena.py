from random import sample
from time import sleep

lista = []

jogos = int(input('Quantos jogos serão gerados: '))

for c in range(1, jogos + 1):
    sublista = sorted(sample(range(1, 60), 6))
    lista.append(sublista)


for i in range(0, jogos):
    print(f'{i+ 1}º jogo {lista[i]}')
    sleep(1)