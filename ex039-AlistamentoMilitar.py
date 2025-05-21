# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alsitar ao serviço militar, se é hora de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
anoNascimento = int(input("Qual ano você nasceu: "))
anoAtual = date.today().year
idade = anoAtual - anoNascimento

if idade < 18:
    print(f"Ainda não é sua hora de se alistar, faltam {18 - idade} anos")
elif idade == 18:
    print("Está na hora de se alistar!")
else:
    print(f"Já estourou o prazo para se alistar em {idade - 18} ano(s)")