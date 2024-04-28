class Restaurante:
    nome = ""
    categoria = ""
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = "Praça"
restaurante_praca.categoria = "Gourmet"
restaurante_pizza = Restaurante()


restaurantes =[restaurante_praca, restaurante_pizza]
print(restaurantes) # exibe o espaço alocado na memória

print(dir(restaurante_praca)) # exibe as informações do objeto
print(vars(restaurante_praca)) # exibe as variaveis em formato de dicionario
