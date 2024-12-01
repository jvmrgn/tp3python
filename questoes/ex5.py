import pandas as pd
import os

arquivo_excel = os.path.join("data", "INFwebNET_Historico.xlsx")

def combinar_arquivos_excel():
    """
    Combina planilhas de um arquivo Excel e exibe o número total de linhas de cada uma.
    Usa try...except para tratar possíveis erros.
    """
    try:
        dados_excel = pd.ExcelFile(arquivo_excel)

        print(f"Planilhas encontradas no arquivo '{arquivo_excel}':\n")
        for planilha in dados_excel.sheet_names:
            dados = dados_excel.parse(planilha)

            print(f"Planilha: {planilha} - Total de linhas: {dados.shape[0]}")
    
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_excel}' não foi encontrado. Certifique-se de que ele está no local correto.")
    except Exception as e:
        print(f"Erro ao carregar o arquivo Excel: {e}")

combinar_arquivos_excel()
