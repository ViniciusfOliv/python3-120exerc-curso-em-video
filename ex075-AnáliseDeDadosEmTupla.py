# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posião foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

cont = 0
tupla = ((int(input('Digite um número: '))),
         int(input('Outro número: ')),
         int(input('Mais um número: ')),
         int(input('Último número: ')))



   
for item in tupla:
    if item % 2 == 0:
        cont += 1

print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 apareceu na posição {tupla.index(3) + 1}º ')
print(f'Os valores pares digitados foram {cont}')