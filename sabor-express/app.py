import os

restaurantes = [
                {"nome": "Praça", "categoria": "Japonesa", "ativo": False},
                {"nome": "Pizza Suprema", "categoria": "Italiana", "ativo": True},
                {"nome": "Cantina", "categoria": "Pizza", "ativo": False}
               ]

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
    categoria = input(f"Digite a categoria do restaurante {nome_restaurante}: ")

    dados_restaurante = {"nome": nome_restaurante, "categoria": categoria, "ativo": False}
    restaurantes.append(dados_restaurante)
    print(f"O restaurante {nome_restaurante} foi cadastrado com sucesso!")
    volta_menu()

def listar_restaurante():
    exibe_subtitulo("Lista de restaurantes\n")

    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = restaurante["ativo"]
        print(f". - {nome_restaurante} | {categoria} | {ativo} ")

    volta_menu()

def alterna_ativo():
    exibe_subtitulo("Alternando estado do restaurante")
    nome_restaurante = input(f"Digite o nome do restaurante que deseja alternar o estado:\n")
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso" if restaurante["ativo"] else f"O restaurante {nome_restaurante} foi desativado com sucesso"
            print(mensagem)

    if not restaurante_encontrado:
        print("O restaurante não foi encontrado no sistema")


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
            alterna_ativo()
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
