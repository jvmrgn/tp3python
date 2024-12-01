import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

engine = create_engine('sqlite:///INFwebNET_DB.db', echo=True)

def recalcular_idade(data_nascimento, data_referencia):
    """
    Função para recalcular a idade de uma pessoa com base na data de nascimento e uma data de referência.
    """
    if pd.isna(data_nascimento):
        return None
    idade = data_referencia.year - data_nascimento.year
    if (data_referencia.month, data_referencia.day) < (data_nascimento.month, data_nascimento.day):
        idade -= 1
    return idade

data_referencia = datetime(2024, 7, 22)

try:
    dados_consolidado = pd.read_sql('SELECT * FROM Consolidado', con=engine)
    print(f"Total de linhas na tabela 'Consolidado': {dados_consolidado.shape[0]}")
    
    dados_consolidado['data de nascimento'] = pd.to_datetime(dados_consolidado['data de nascimento'], errors='coerce')
    
    dados_consolidado['idade'] = dados_consolidado['data de nascimento'].apply(lambda x: recalcular_idade(x, data_referencia))

    dados_consolidado.to_sql('Consolidado_Atualizado', con=engine, if_exists='replace', index=False)
    print("Tabela 'Consolidado_Atualizado' criada com os dados atualizados.")
    
except Exception as e:
    print(f"Erro ao tentar atualizar a idade e salvar os dados: {e}")
