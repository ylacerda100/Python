
agenda = []


def adicionar():
    nome = (input('Digite o nome do contato: '))
    numero = input('Digite o telefone do contato: ')
    agenda.append([nome, numero])
    print('Contato adicionado com sucesso.')


def modificar():
    if len(agenda) == 0:
        print('Agenda vazia. Por favor adicione contatos para realizar esta ação.')
    else:
        pesquisa = input('Digite o nome do contato que deseja modificar: ')
        pesquisa = pesquisa.lower()
        for c, n in enumerate(agenda):
            if n[0].lower() == pesquisa:
                print(f'Contato encontrado.\nNome: {c} === Telefone: {n}')
                nome = (input('Digite o novo nome do contato: '))
                numero = input('Digite o novo telefone do contato: ')
                agenda[c] = [nome, numero]
                print('Contato modificado.')
            else:
                print('Contato não encontrado')


def excluir():
    if len(agenda) == 0:
        print('Agenda vazia. Por favor adicione contatos para realizar esta ação.')
    else:
        nome_excluir = input('Digite o nome do contato que deseja excluir: ')
        nome_excluir = nome_excluir.lower()
        for c, n in enumerate(agenda):
            if n[0].lower() == nome_excluir:
                del agenda[c]
                print('Contato excluído com sucesso')
            else:
                print('Contato não encontrado')



def listar():
    if len(agenda) == 0:
        print('Agenda vazia')
    else:
        for contato in agenda:
            print(f'Nome: {contato[0]} ===== Telefone: {contato[1]}')


def main():

    print('=== Agenda ===\nEscolha uma das opções:')
    while True:
        option = int(input('(1) Adicionar contato\n(2) Modificar contato\n(3) Excluir contato\n'
                           '(4) Listar contatos\n(5) Sair\nDigite: '))
        if option == 1:
            adicionar()
        elif option == 2:
            modificar()
        elif option == 3:
            excluir()
        elif option == 4:
            listar()
        elif option == 5:
            print('Saindo da agenda...')
            break
        else:
            print('Opção inválida! Tente novamente.')


main()
