import pandas as pd
import os
from sqlalchemy import create_engine

arquivo_excel = os.path.join("data", "INFwebNET_Historico.xlsx")

arquivo_salvo = os.path.join("data", "dados_combinados.xlsx")

def combinar_e_limpar_arquivos_excel():
    """
    Carrega as planilhas de um arquivo Excel, combina as informações e remove duplicatas com base na coluna "id".
    """
    try:
        dados_excel = pd.ExcelFile(arquivo_excel)

        dados_2022 = dados_excel.parse("INFwebNET2022")
        dados_2023 = dados_excel.parse("INFwebNET2023")

        print(f"Planilha INFwebNET2022 - Total de linhas: {dados_2022.shape[0]}")
        print(f"Planilha INFwebNET2023 - Total de linhas: {dados_2023.shape[0]}")

        dados_combinados = pd.concat([dados_2022, dados_2023], ignore_index=True)

        dados_combinados = dados_combinados.drop_duplicates(subset="id")

        print(f"Total de linhas após a combinação e remoção de duplicatas: {dados_combinados.shape[0]}")
        
        dados_combinados.to_excel(arquivo_salvo, index=False)
        print(f"Dados combinados salvos em: {arquivo_salvo}")
        
        return dados_combinados
    
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_excel}' não foi encontrado. Certifique-se de que ele está no local correto.")
    except Exception as e:
        print(f"Erro ao carregar o arquivo Excel: {e}")
    
    return None

def carregar_dados_sqlite(dados_combinados):
    """
    Conecta-se ao banco de dados SQLite e carrega os dados combinados para a tabela "Usuarios_Historicos".
    Se o banco de dados não existir, ele será criado automaticamente.
    """
    try:
        engine = create_engine(f"sqlite:///INFwebNET_DB.db")

        dados_combinados.to_sql("Usuarios_Historicos", con=engine, if_exists="replace", index=False)

        print("Dados carregados com sucesso para a tabela 'Usuarios_Historicos'!")
    
    except Exception as e:
        print(f"Erro ao carregar dados no banco de dados: {e}")

dados_combinados = combinar_e_limpar_arquivos_excel()

if dados_combinados is not None:
    carregar_dados_sqlite(dados_combinados)

    print("\nPrévia dos dados combinados:")
    print(dados_combinados.head())
