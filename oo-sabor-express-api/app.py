import os
import requests
import json

url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"

resp = requests.get(url)
print(resp)

if resp.status_code == 200:
    json_data = resp.json()

    # Criar dicionário para adicionar os restaurantes
    dados_restaurante = {}

    for item in json_data:
        nome_restaurante = item["Company"]
        if nome_restaurante not in dados_restaurante:
            dados_restaurante[nome_restaurante] = []

        dados_restaurante[nome_restaurante].append({
            "item": item['Item'],
            "price": item['price'],
            "description": item['description']
        })

    pasta_api = "dados-api"
    if not os.path.exists(pasta_api):
        os.makedirs(pasta_api)

else:
    print(f"O erro foi {resp.status_code}")



for nome_restaurante, dados in dados_restaurante.items():
    nome_arquivo = f'{pasta_api}/{nome_restaurante}.json'
    with open(nome_arquivo, 'w') as arquivo_restaurantes:
        json.dump(dados, arquivo_restaurantes, indent=4)
