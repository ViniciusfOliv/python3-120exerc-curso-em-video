while True:
    print('-' * 10)
    tabuada = int(input('Qual número você quer ver a tabuada?: '))
    print('-' * 10)

    if tabuada < 0:
        break
    for c in range(1, 11):
        print(f'{tabuada} x {c} = {tabuada * c} ')