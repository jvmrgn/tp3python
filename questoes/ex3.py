import pandas as pd
import os

arquivo_csv = os.path.join("data", "dados_usuarios.csv")
arquivo_excel = os.path.join("data", "INFwebNET_30mais.xlsx")

def filtrar_e_salvar():
    """
    Seleciona usuários com idade maior que 30 e salva os dados em um arquivo Excel.
    """
    try:
        dados = pd.read_csv(arquivo_csv, delimiter=';')

        usuarios_30mais = dados[dados['idade'] > 30]

        if usuarios_30mais.empty:
            print("Nenhum usuário com idade maior que 30 foi encontrado.")
            return

        usuarios_30mais.to_excel(arquivo_excel, index=False, engine='openpyxl')

        print(f"Os dados dos usuários com idade maior que 30 foram salvos em '{arquivo_excel}'.")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_csv}' não foi encontrado. Certifique-se de que ele está no local correto.")
    except KeyError as e:
        print(f"Erro: A coluna especificada não foi encontrada no arquivo. Detalhes: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

filtrar_e_salvar()
