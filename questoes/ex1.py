import pandas as pd
import os

arquivo = os.path.join("data", "dados_usuarios.csv")

def carregar_dados():
    """
    Tenta carregar os dados do arquivo CSV.
    Exibe uma mensagem de erro específica caso o arquivo não seja encontrado.
    Trata problemas de leitura com delimitador.
    """
    try:
        dados = pd.read_csv(arquivo, delimiter=';')
        print("Arquivo carregado com sucesso!")
        return dados
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo}' não foi encontrado. Certifique-se de que ele está no local correto.")
    except pd.errors.ParserError as e:
        print(f"Erro ao tentar carregar o arquivo: Problema de formatação. Detalhes: {e}")
    except Exception as e:
        print(f"Erro inesperado ao tentar carregar o arquivo: {e}")
    return None

dados = carregar_dados()

if dados is not None:
    print("\nPrévia dos dados:")
    print(dados.head())
else:
    print("\nNão foi possível carregar os dados. O exercício será pulado.")
