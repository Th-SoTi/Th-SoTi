from time import sleep #IMPORT DE TEMPO PARA PAUSAS NO ALGORITMO
import os # IMPORT DE LIMPAR TERMINAL
biblioteca = [] #USADO PARA O APPEND

def intro(): #BASICAMENTE O MENU PRINCIPAL
    print("---Bem vindo a Biblioteca Online---")
    print("1. Adicionar um novo livro")
    print("2. Visualizar a lista de livros")
    print("3. Buscar um livro pelo título")
    print("4. Encerrar")
    print("-----------------------------------\n")


def add_livro(): # USADO PARA ADD UM LIVRO
    titulo = input("Digite o titulo do livro: ")
    autor = input("Digite o nome do autor: ")
    ano = input("Digite o ano do livro: ")
    
    livro = {
        "Titulo": titulo,
        "Autor": autor,
        "Ano": ano
    }

    biblioteca.append(livro)
    print("Livro registrado com Sucesso!!!")

    sleep(3)
    os.system('cls')

def exibir_liv(): # USADO PARA EXIBIR TODOS OS LIVROS
    if biblioteca:
        print("\nLista de Livros:")
        for i, livro in enumerate(biblioteca, start=1):
            print(f"\n{i}. Livro")
            print(f" Título: {livro['Titulo']}")
            print(f" Autor: {livro['Autor']}")
            print(f" Ano: {livro['Ano']}")
    else:
        print("\nA biblioteca está vazia.\n")
    voltar_ao_menu()

def procurar_liv(): #USADO PARA PROCURAR O LIVRO
    titulo_procurado = input("Digite o titulo que deseja buscar: ")
    
    for livro in biblioteca:
        if livro["Titulo"].lower() == titulo_procurado.lower():
            print("\nLivro encontrado:")
            print(f"Titulo: {livro['Titulo']}")
            print(f"Autor: {livro['Autor']}")
            print(f"Ano: {livro['Ano']}")
            voltar_ao_menu()
            return
    print("\nLivro não encontrado na biblioteca!!!\n")
    voltar_ao_menu()

def voltar_ao_menu():
    input("\nPressione Enter para voltar ao menu principal.")
    os.system('cls')


while True:
    intro()
    try:
        opcao = int(input("Digite a opção: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        sleep(2)
        os.system('cls')
        continue

    if opcao == 1:
        os.system('cls')
        add_livro()
    elif opcao == 2:
        os.system('cls')
        exibir_liv()
    elif opcao == 3:
        os.system('cls')
        procurar_liv()
    elif opcao == 4:
        print("THE END")
        break
    else:
        print("Opção inválida!")
        sleep(2)
        os.system('cls')