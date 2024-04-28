class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"{self.nome} | {self.categoria}"

    def listar_restaurante():
        for restaurante in restaurantes:
            print(f'Restaurante {restaurante.nome} | Categoria: {restaurante.categoria} | Ativo: {restaurante.ativo}')

restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_pizza = Restaurante("Pizza Express", "Italiano")


restaurantes =[restaurante_praca, restaurante_pizza]
print(restaurantes) # exibe o espaço alocado na memória

print(dir(restaurante_praca)) # exibe as informações do objeto
print(vars(restaurante_praca)) # exibe as variaveis em formato de dicionario
print(vars(restaurante_pizza)) # exibe as variaveis em formato de dicionario

# apos a criação do metodo __str__
print(restaurante_praca)


Restaurante.listar_restaurante()
