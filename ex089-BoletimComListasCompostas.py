lista = list()

while True:
    nome = input('Nome: ')
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    sublista = [nome, [nota_1, nota_2]]
    lista.append(sublista)
   
    continuar = input('Quer continuar [S/N]: ').upper()
    while continuar not in 'SN':
        continuar = input('Quer continuar [S/N]: ').upper()

    if continuar == 'N':
        break

for i in range(0, len(lista)):
   print(f'{i}', end=' ')
   print(f'{lista[i][0]}', end=' ')
   print(f'{sum(lista[i][1]) / 2}')

escolha = 0
while escolha != 999:
    escolha = int(input('Escolha um aluno para momstrar as notas [999 para interromper]: '))
    print(f'O aluno {lista[escolha][escolha]} tirou a nota {lista[escolha][1]}')
    