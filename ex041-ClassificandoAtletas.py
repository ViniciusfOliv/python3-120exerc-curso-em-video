# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade.
# Até 9 anos: Mirim
# Até 14 anos: Infantil
# Até 19 anos: Junior
# Até 25 anos: Sênior
# Acima: Master

from datetime import date
ano_nasc = int(input("Digite seu ano de nascimento: "))
ano_atual = date.today().year
idade = ano_atual - ano_nasc

if idade <= 9:
    print('Você é um atleta Mrrim')
elif idade <= 14:
    print('Você é um atleta Infantil')
elif idade <= 19:
    print('Você é um atleta Junior')
elif idade <= 25:
    print('Você é um atleta Sênior')
else:
    print('Você é um atleta Master')