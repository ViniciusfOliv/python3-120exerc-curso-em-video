lista = []
cont_esq = 0
cont_dir = 0

lista.append(input('Digite uma expressão matematica: '))
for item in lista:
    for letra in item:
        if letra == '(':
            cont_esq += 1
        elif letra == ')':
            cont_dir += 1


if cont_dir == cont_esq:
    print('Temos uma expressão válida!')
else:
    print('Não é uma expressão válida!')