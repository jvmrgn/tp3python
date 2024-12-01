import pandas as pd
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

dados_combinados = combinar_e_limpar_arquivos_excel()

if dados_combinados is not None:
    print("\nPrévia dos dados combinados:")
    print(dados_combinados.head())
