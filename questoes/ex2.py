import pandas as pd
import os

arquivo = os.path.join("data", "dados_usuarios.csv")

def explorar_dados():
    """
    Carrega o arquivo CSV, exibe as 10 primeiras linhas e lista as colunas presentes no arquivo.
    """
    try:
        dados = pd.read_csv(arquivo, delimiter=';')
        
        print("As 10 primeiras linhas do arquivo são:\n")
        print(dados.head(10))

        print("\nAs colunas presentes no arquivo são:")
        for coluna in dados.columns:
            print(f"- {coluna}")
            
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo}' não foi encontrado. Certifique-se de que ele está no local correto.")
    except pd.errors.ParserError as e:
        print(f"Erro ao tentar carregar o arquivo: Problema de formatação. Detalhes: {e}")
    except Exception as e:
        print(f"Erro inesperado ao tentar carregar o arquivo: {e}")

explorar_dados()
