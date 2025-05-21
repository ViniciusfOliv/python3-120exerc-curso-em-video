'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastrre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados em ordem crescente.'''
lista_num = []
while True:
    num = int(input('Valor: '))
    if num not in lista_num:
        print('Número adicionado a lista.')
        lista_num.append(num)
    else:
        print('Número já existe na lista, tente outro')

    continuar = input('Quer continuar? [S/N]: ').strip().upper()
    if continuar == 'N':
        break
   
print('Os valores digitados em ordem crescente foram')
print(sorted(lista_num))