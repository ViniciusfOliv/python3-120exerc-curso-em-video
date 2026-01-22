# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

ano_atual = date.today().year
cont_maior = 0 
cont_menor = 0

for i in range(1, 8): 
    data_nasc = int(input(f'Digita a {i}ª data de nascimento: '))
    maioridade = ano_atual - data_nasc
    if maioridade >= 21:
        cont_maior += 1
    else:
        cont_menor += 1

print(f'Você tem {cont_maior} pessoas maior de idade e {cont_menor} pessoas menor de idade')

