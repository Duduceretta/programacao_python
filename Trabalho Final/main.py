import requests
import os
from dotenv import load_dotenv
from typing import List, Optional
from cidade_clima import CidadeClima

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def buscar_clima(cidade: str, api_key: str) -> Optional[CidadeClima]:
    """
    Função responsável por fazer a requisição HTTP e consumir os dados da API.
    """
    params = {
        "q": cidade,
        "appid": api_key,
        "units": "metric",
        "lang": "pt_br"
    }

    try:
        resposta = requests.get(BASE_URL, params=params, timeout=10)
        
        if resposta.status_code == 404:
            print(f"Erro: A cidade '{cidade}' não foi encontrada. Verifique se o nome foi digitado corretamente.")
            return None
            
        elif resposta.status_code == 401:
            print("Erro de Autenticação: API Key está inválida ou ainda não foi ativada pelos servidores.")
            return None

        resposta.raise_for_status()

        dados_json = resposta.json()

        nome_formatado = dados_json["name"]
        temperatura = dados_json["main"]["temp"]
        umidade = dados_json["main"]["humidity"]
        condicao = dados_json["weather"][0]["description"]

        return CidadeClima(
            nome=nome_formatado,
            temperatura=temperatura,
            umidade=umidade,
            condicao=condicao
        )

    except requests.exceptions.Timeout:
        print(f"⏳ Erro de Conexão: O tempo limite de resposta para a cidade '{cidade}' foi esgotado.")
        return None
    except requests.exceptions.RequestException as erro:
        print(f"❌ Erro de Rede inesperado ao buscar '{cidade}': {erro}")
        return None


def main():
    lista_cidades = ["São Paulo", "London", "Tokyo", "New York", "Paris"]
    
    relatorio_clima: List[CidadeClima] = []

    print("Iniciando a consulta ao Sistema de Monitoramento Climático...\n")

    for cidade in lista_cidades:
        print(f"Buscando dados de {cidade}...")
        objeto_clima = buscar_clima(cidade, API_KEY)
        
        if objeto_clima is not None:
            relatorio_clima.append(objeto_clima)

    print("\n" + "📊" * 15)
    print("      RELATÓRIO CLIMÁTICO FINAL")
    print("📊" * 15)

    if not relatorio_clima:
        print("\nNenhum dado pôde ser carregado no relatório.")
    else:
        for cidade_objeto in relatorio_clima:
            print(cidade_objeto)


if __name__ == "__main__":
    main()