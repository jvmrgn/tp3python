import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime
import os

arquivo_excel = os.path.join("data", "INFwebNET_Historico.xlsx")

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

        return dados_combinados

    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_excel}' não foi encontrado. Certifique-se de que ele está no local correto.")
    except Exception as e:
        print(f"Erro ao carregar o arquivo Excel: {e}")

    return None

def recalcular_idade(data_nascimento, data_referencia):
    """
    Recalcula a idade com base na data de nascimento e a data de referência fornecida.
    """
    if pd.isna(data_nascimento):
        return None
    idade = data_referencia.year - data_nascimento.year
    if (data_referencia.month, data_referencia.day) < (data_nascimento.month, data_nascimento.day):
        idade -= 1
    return idade

dados_combinados = combinar_e_limpar_arquivos_excel()

if dados_combinados is not None and not dados_combinados.empty:
    try:
        data_referencia = datetime(2024, 7, 22)

        dados_combinados['data_nascimento'] = pd.to_datetime(dados_combinados['data_nascimento'], errors='coerce')

        dados_combinados['idade'] = dados_combinados['data_nascimento'].apply(lambda x: recalcular_idade(x, data_referencia))

        engine = create_engine('sqlite:///INFwebNET_DB.db', echo=True)

        dados_combinados.to_sql('Consolidado', con=engine, if_exists='replace', index=False)
        
        print("Tabela 'Consolidado' criada e dados inseridos com sucesso, incluindo a coluna 'idade'.")

    except Exception as e:
        print(f"Erro ao tentar salvar os dados na tabela 'Consolidado': {e}")
else:
    print("Não há dados para inserir na tabela 'Consolidado'.")
