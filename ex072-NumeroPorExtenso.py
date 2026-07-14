# Crie um programa que tenha uma tupla totamente preenchida com uma contatem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostra-lo por extenso.

tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze','Doze', 'Treze', 'Quatorze','Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')


num = int(input('Digite um número entre 0 e 20: '))
while num > 20 or num < 0:
    num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    
print(f'Você digitou o número {tupla[num]}')
