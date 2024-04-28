class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = int(ano)

class Restaurante:
    def __init__(self, nome, categoria, endereco, cidade):
        self.nome = nome
        self.categoria = categoria
        self.endereco = endereco
        self.cidade = cidade
        self.ativo = False

    def __str__(self):
        return f"nome: {self.nome}, categoria: {self.categoria}"

praca = Restaurante("Praça", "Gourmet", "Av. Bolinha", "Indianápolis")
print(praca)

class Cliente:
    def __init__(self, nome='', idade=0, email='', telefone=''):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone

# Instanciando três objetos da classe Cliente e atribuindo valores aos seus atributos através do construtor
cliente1 = Cliente(nome='Alice', idade=25, email='alice@gmail.com', telefone='123-456-7890')
cliente2 = Cliente(nome='Bob', idade=30, email='bob@gmail.com', telefone='987-654-3210')
cliente3 = Cliente(nome='Charlie', idade=22, email='charlie@gmail.com', telefone='555-123-4567')
