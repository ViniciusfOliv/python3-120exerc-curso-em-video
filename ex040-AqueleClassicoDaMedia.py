# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final de acordo com a média atingida:

print("Boletim escolar!")
nome = input("Nome: ")
n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
media = (n1 + n2) / 2

if media < 5:
    print(f'Caro {nome}, infelizmente você está reprovado, sua média foi {media}')

elif media < 7:
    print(f'Caro {nome}, você está de recuperação, sua média é {media}')

else:
    print(f'Parabéns {nome}, você foi aprovado! sua média é {media}')
