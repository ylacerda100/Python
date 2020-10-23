def validar(a, b):
    if a.isalpha() == False and b.isalpha() == False:
        return True
    else:
        return False



def adicao(a,b):
    if validar(a, b):
        a = float(a)
        b = float(b)
        resultado = a + b
        print(f'O resultado é {resultado}')
    else:
        print('ERRO! Por favor, digite números válidos.')


def subtracao(a,b):
    if validar(a, b):
        a = float(a)
        b = float(b)
        resultado = a - b
        print(f'O resultado é {resultado}')
    else:
        print('ERRO! Por favor, digite números válidos.')


def multiplica(a,b):
    if validar(a, b):
        a = float(a)
        b = float(b)
        resultado = a * b
        print(f'O resultado é {resultado}')
    else:
        print('ERRO! Por favor, digite números válidos.')


def divisao(a,b):
    if validar(a, b):
        a = float(a)
        b = float(b)
        resultado = a / b
        print(f'O resultado é {resultado}')
    else:
        print('ERRO! Por favor, digite números válidos.')


def main():
    while True:
        print('====== CALCULADORA ======')
        print('Escolha a operação desejada ou digite "zero" para sair:')
        print('(1) Adição\n(2) Subtração\n(3) Multiplicação\n(4) Divisão')
        option = input('Digite: ')
        if option == 'zero':
            print('Saindo do programa...')
            break
        else:
            numero_1 = input('Digite um número: ')
            numero_2 = input('Digite outro número: ')
            if option == '1':
                adicao(numero_1, numero_2)
            elif option == '2':
                subtracao(numero_1, numero_2)
            elif option == '3':
                multiplica(numero_1, numero_2)
            elif option == '4':
                divisao(numero_1, numero_2)
            else:
                print('Opção inválida! Por favor, escolha uma operação válida.')

main()
