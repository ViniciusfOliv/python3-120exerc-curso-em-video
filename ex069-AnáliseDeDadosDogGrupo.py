cont_idade = 0
cont_homens = 0
cont_mulheres = 0
sexo = ''

while True:
    print('-' * 20)
    print('Cadastre uma pessoa')
    print('-' * 20)

    idade = int(input('Idade: '))
    sexo = input('M/F: ').upper()
    while sexo not in 'MF':
        print('Digite o sexo corretamente!')
        sexo = input('M/F: ').upper()
    
    if idade > 18:
        cont_idade += 1
        
    if sexo == 'M':
        cont_homens += 1

    if sexo == 'F' and idade < 20:
        cont_mulheres += 1

    continuar = input('Quer continuar? [S/N]: ').upper()
    while continuar not in 'SN':
        print('Digite corretamente!')
        continuar = input('Quer continuar? [S/N]: ').upper()

    if continuar == 'S':
        continue
    elif continuar == 'N':
        break

print(f'{cont_idade} pessoas tem mais de 18 anos\n{cont_homens} homens foram cadastrados\n{cont_mulheres} mulheres tem menos de 20 anos.')
    
    