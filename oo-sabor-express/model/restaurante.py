class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"{self._nome} | {self._categoria}"

    @classmethod
    def listar_restaurante(cls):
        print(f"{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | Status")
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Desativado'

    def alternar_estado(self):
        self._ativo = not self._ativo

restaurante_praca = Restaurante("praça", "gourmet")
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante("pizza express", "italiano")


restaurantes =[restaurante_praca, restaurante_pizza]
print(restaurantes) # exibe o espaço alocado na memória

print(dir(restaurante_praca)) # exibe as informações do objeto
print(vars(restaurante_praca)) # exibe as variaveis em formato de dicionario
print(vars(restaurante_pizza)) # exibe as variaveis em formato de dicionario

# apos a criação do metodo __str__
print(restaurante_praca)


Restaurante.listar_restaurante()