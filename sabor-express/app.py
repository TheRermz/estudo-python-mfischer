import os

restaurantes = ["Pizza", "Sushi"]

def volta_menu():
    input("\nDigite uma tecla para voltar ao menu principal: ")
    main()

def exibe_subtitulo(texto):
    os.system("clear")
    print(texto)

def exibir_nome_programa():
    print("Sabor Express\n")

def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Ativar restaurante")
    print("4. Sair\n")

def finalizar_app():
    exibe_subtitulo("Finalizar app")

def cadastrar_restaurante():
    exibe_subtitulo("Cadastro de novos restaurantes")
    nome_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")

    restaurantes.append(nome_restaurante)
    print(f"O restaurante {nome_restaurante} foi cadastrado com sucesso!")
    volta_menu()

def listar_restaurante():
    exibe_subtitulo("Lista de restaurantes\n")

    for restaurante in restaurantes:
        print(f". - {restaurante}")

    volta_menu()

def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        # print("Você escolheu a opção", opcao_escolhida)
        # # fstring --> interpolação de strings
        # print(f"Você escolheu a opção {opcao_escolhida}")

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurante()
        elif opcao_escolhida == 3:
            print("Ativar restaurante")
        else:
            finalizar_app()
    except:
        print("Digite um valor válido!")
        volta_menu()

def main():
    os.system("clear")
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()
