import pandas as pd
import os

arquivo = os.path.join("data", "dados_usuarios.csv")

def limpar_dados():
    """
    Realiza a limpeza de dados no arquivo CSV, conforme os requisitos:
    1. Remove usuários sem e-mail válido.
    2. Preenche valores ausentes na coluna "cidade" com "Não Informada".
    3. Preenche valores ausentes na coluna "estado" com "ZZ".
    """
    try:
        dados = pd.read_csv(arquivo, delimiter=';')

        dados = dados[dados['email'].notnull()]

        dados['cidade'] = dados['cidade'].fillna("Não Informada")

        dados['estado'] = dados['estado'].fillna("ZZ")

        print("\nDados após a limpeza:")
        print(dados.head())

        arquivo_limpo = os.path.join("data", "dados_usuarios_limpos.csv")
        dados.to_csv(arquivo_limpo, index=False, sep=';')
        print(f"\nDados limpos salvos em: {arquivo_limpo}")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo}' não foi encontrado. Certifique-se de que ele está no local correto.")
    except Exception as e:
        print(f"Erro ao processar os dados: {e}")

limpar_dados()