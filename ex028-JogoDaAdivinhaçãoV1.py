# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint

print("Tente adivinhar o número que o computador pensou! hehe")
usuario = int(input("Digite um número inteiro entre 0 e 5: "))
computador = randint(0, 5)

if usuario == computador:
    print(f"Você adivinhou! o computador pensou no número {computador}")
else:
    print(f"Você errou! o computador pensou no número {computador}")