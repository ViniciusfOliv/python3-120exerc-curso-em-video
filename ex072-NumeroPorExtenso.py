# Crie um programa que tenha uma tupla totamente preenchida com uma contatem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostra-lo por extenso.

tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',' Doze', 'Treze', 'Quatorze',' Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    num = int(input('Escolha um número de 0 a 20: '))
    if 0 <= num <= 20:
        break
    print('Número inválido, tente novamente.')
print(f'Você escolheu o número {tupla[num]}')