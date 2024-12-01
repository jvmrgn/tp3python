import os
import pandas as pd
import sqlite3

def ler_arquivos():
    """
    Função para ler diversos tipos de arquivos (CSV, Excel, SQLite e TXT) presentes
    no diretório do projeto e processá-los conforme o tipo. O processo inclui leitura,
    exibição de informações sobre o arquivo e tratamento de exceções para erros comuns.

    A função percorre uma lista de arquivos esperados, verifica sua existência no sistema
    de arquivos, e realiza a leitura com os devidos métodos baseados na extensão do arquivo.
    """

    arquivos = [
        "dados_usuario.csv",
        "INFwebNET_30mais.xlsx",
        "INFwebNET_Historico.xlsx",
        "INFwebNET_DB.db",
        "dados_ausentes.txt"
    ]

    for arquivo in arquivos:
        if arquivo in ["INFwebNET_DB.db", "dados_ausentes.txt"]:
            caminho_arquivo = os.path.join(os.getcwd(), arquivo)
        else:
            caminho_arquivo = os.path.join("data", arquivo)

        print(f"Tentando ler o arquivo: {caminho_arquivo}")
        
        if not os.path.exists(caminho_arquivo):
            print(f"Erro: O arquivo '{arquivo}' não foi encontrado no diretório. Verifique o caminho.")
            continue
        
        try:
            if arquivo.endswith('.csv'):
                dados_csv = pd.read_csv(caminho_arquivo, encoding='ISO-8859-1')
                print(f"Arquivo '{arquivo}' lido com sucesso. Linhas: {len(dados_csv)}")
            
            elif arquivo.endswith('.xlsx'):
                dados_excel = pd.ExcelFile(caminho_arquivo)
                for sheet_name in dados_excel.sheet_names:
                    dados = dados_excel.parse(sheet_name)
                    print(f"Planilha '{sheet_name}' do arquivo '{arquivo}' lida com sucesso. Linhas: {dados.shape[0]}")

            elif arquivo.endswith('.db'):
                conn = sqlite3.connect(caminho_arquivo)
                cursor = conn.cursor()
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                tables = cursor.fetchall()
                print(f"Banco de dados '{arquivo}' lido com sucesso. Tabelas: {len(tables)}")
                conn.close()

            elif arquivo.endswith('.txt'):
                with open(caminho_arquivo, 'r', encoding='ISO-8859-1') as f:
                    dados_txt = f.readlines()
                    print(f"Arquivo '{arquivo}' lido com sucesso. Linhas: {len(dados_txt)}")

        except FileNotFoundError as e:
            print(f"Erro: O arquivo '{arquivo}' não foi encontrado. Detalhes: {e}")
        except MemoryError as e:
            print(f"Erro de memória ao tentar ler o arquivo '{arquivo}'. Detalhes: {e}")
        except RuntimeError as e:
            print(f"Erro de execução ao tentar ler o arquivo '{arquivo}'. Detalhes: {e}")
        except EOFError as e:
            print(f"Erro de fim de arquivo inesperado ao tentar ler o arquivo '{arquivo}'. Detalhes: {e}")
        except OSError as e:
            print(f"Erro de sistema ao tentar acessar o arquivo '{arquivo}'. Detalhes: {e}")
        except ConnectionError as e:
            print(f"Erro de conexão ao tentar acessar o arquivo '{arquivo}'. Detalhes: {e}")
        except TimeoutError as e:
            print(f"Erro de timeout ao tentar acessar o arquivo '{arquivo}'. Detalhes: {e}")
        except PermissionError as e:
            print(f"Erro de permissão ao tentar acessar o arquivo '{arquivo}'. Detalhes: {e}")
        
        else:
            print(f"Arquivo '{arquivo}' processado com sucesso e as informações foram carregadas.")
        
        finally:
            print(f"Processamento do arquivo '{arquivo}' concluído.\n")

ler_arquivos()
