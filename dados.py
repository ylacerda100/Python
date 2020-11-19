from random import randint

while True:
    op = input('Deseja rolar o dado? (S/N)').lower()
    if op == 's':
        print(randint(1, 6))
    elif op == 'n':
        print('Saindo...')
        break
    else:
        print('Por favor, digite um caracter válido.')