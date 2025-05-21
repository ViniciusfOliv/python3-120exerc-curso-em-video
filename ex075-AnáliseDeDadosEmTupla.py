# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posião foi digitado o primeiro valor 3.
# C) Quais foram os números pares.


valores = (int(input('Primeiro valor: ')),
            int(input('Segundo valor: ')),
            int(input('Terceiro valor: ')),
            int(input('Quarto valor: ')))

if 9 in valores:
    print(f'O número nove apareceu {valores.count(9)} vezes')
else:
    print('Não existe numero 9')

if 3 in valores:
    print(f'O primeiro valor 3 está na posição {valores.index(3)}')
else:
    print('Não existe número 3')

print('Verificando números pares: ')
for num in valores:
    if num % 2 == 0:
        print(f'{num} é par')
    else:
        print(f'Não existem números pares')
        break