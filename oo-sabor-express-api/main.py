import os
from fastapi import FastAPI, Query
import requests

app = FastAPI()


@app.get("/api/hello")
def hello_world():
    """
        Exibe hello:world
    """
    return {"hello":"world"}


@app.get("/api/restaurante/")
def get_restaurantes(restaurante: str = Query(None)):
    """
        exibe os restaurantes, se com query, apenas o restaurante selecionado
    """
    url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"

    resp = requests.get(url)


    if resp.status_code == 200:
        json_data = resp.json()

        if restaurante is None:
            return {"Dados": json_data}

        # Criar dicionário para adicionar os restaurantes
        dados_restaurante = []

        for item in json_data:
            nome_restaurante = item["Company"]
            if item["Company"] == restaurante:
               dados_restaurante.append({
                "item": item['Item'],
                "price": item['price'],
                "description": item['description']
            })

        return{"Restaurante": restaurante, "Cardápio": dados_restaurante}


    else:
        return {"Erro":f"{resp.status_code} -- {resp.text}"}
