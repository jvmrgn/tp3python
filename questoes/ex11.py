import pandas as pd
from sqlalchemy import create_engine
import numpy as np

class DadosAusentesError(Exception):
    """
    Exceção personalizada para indicar que dados ausentes foram encontrados para um determinado e-mail.
    """
    def __init__(self, email, message="Dados ausentes encontrados"):
        self.email = email
        self.message = message
        super().__init__(self.message)

def adicionar_dados_ausentes():
    """
    Função para adicionar dados ausentes em uma tabela no banco de dados SQLite 'INFwebNET_DB.db'.
    
    A função seleciona a tabela 'Consolidado' e insere valores ausentes em campos específicos.
    Após a alteração, os dados são regravados na tabela 'Consolidado'.
    """
    engine = create_engine('sqlite:///INFwebNET_DB.db', echo=True)

    try:
        dados_consolidado = pd.read_sql('SELECT * FROM Consolidado', con=engine)

        dados_consolidado.loc[0, 'email'] = "joaovini100@gmail.com"
        dados_consolidado.loc[1, 'data_nascimento'] = np.nan

        dados_consolidado.to_sql('Consolidado', con=engine, if_exists='replace', index=False)
        print("Dados ausentes inseridos com sucesso.")
    
    except Exception as e:
        print(f"Erro ao adicionar dados ausentes: {e}")

def verificar_dados_ausentes():
    """
    Função para verificar se existem dados ausentes na tabela 'Consolidado' do banco de dados SQLite 'INFwebNET_DB.db'.
    
    A função percorre as linhas da tabela e, se encontrar um valor ausente (NaN), levanta uma exceção personalizada
    (DadosAusentesError) para o e-mail associado ao dado ausente.

    Quando dados ausentes são encontrados, o e-mail correspondente é registrado em um arquivo de texto chamado 'dados_ausentes.txt'.
    """
    engine = create_engine('sqlite:///INFwebNET_DB.db', echo=True)

    try:
        dados_consolidado = pd.read_sql('SELECT * FROM Consolidado', con=engine)

        for index, row in dados_consolidado.iterrows():
            if row.isnull().any():
                email_ausente = row['email']
                raise DadosAusentesError(email_ausente)

    except DadosAusentesError as e:
        with open('dados_ausentes.txt', 'a') as file:
            file.write(f"E-mail com dados ausentes: {e.email}\n")
        print(f"Dados ausentes encontrados para o e-mail: {e.email}")
    
    except Exception as e:
        print(f"Erro ao verificar dados ausentes: {e}")

adicionar_dados_ausentes()
verificar_dados_ausentes()
