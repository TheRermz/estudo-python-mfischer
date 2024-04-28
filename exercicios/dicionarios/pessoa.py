# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

# 2 - Utilizando o dicionário criado no item 1:

#     Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
#     Adicione um campo de profissão para essa pessoa;
#     Remova um item do dicionário.

pessoas = [
    {"nome":  "Ana Julia", "idade": "19", "cidade": "Limeira"},
    {"nome":  "Camila", "idade": "18", "cidade": "Limeira"},
    {"nome":  "Murilo", "idade": "26", "cidade": "Araras"}
]

for pessoa in pessoas:
    nome = pessoa["nome"]
    idade = pessoa["idade"]
    cidade = pessoa["cidade"]
    profissao = pessoa.update({"profissão": "TI"}) # adicionar campo na tabela
    print(f'{nome}, {idade}, {cidade}, {profissao}')

    # alterar dado no dicionario
    if(nome == "Ana Julia"):
        idade = 20

    if(nome == "Murilo"):
        profissao = "desempregado"


    del pessoa["cidade"]

    print(f'EDITADO {nome}, {idade}, {cidade}, {profissao}')

pessoas.pop(2) # remover um item do dicionáriio
print(pessoas)
