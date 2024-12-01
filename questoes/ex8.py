import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

engine = create_engine('sqlite:///INFwebNET_DB.db', echo=True)

def recalcular_idade(data_nascimento, data_referencia):
    if pd.isna(data_nascimento):
        return None
    idade = data_referencia.year - data_nascimento.year
    if (data_referencia.month, data_referencia.day) < (data_nascimento.month, data_nascimento.day):
        idade -= 1
    return idade

data_referencia = datetime(2024, 7, 22)

try:
    usuarios_historicos = pd.read_sql('SELECT * FROM Usuarios_Historicos', con=engine)
    
    usuarios_historicos['data de nascimento'] = pd.to_datetime(usuarios_historicos['data de nascimento'], errors='coerce')
    
    usuarios_historicos['idade'] = usuarios_historicos['data de nascimento'].apply(lambda x: recalcular_idade(x, data_referencia))
    
    usuarios_filtrados = usuarios_historicos[(usuarios_historicos['idade'] >= 22) & (usuarios_historicos['idade'] <= 30)]
    
    print(usuarios_filtrados)

except Exception as e:
    print(f"Erro ao tentar buscar os dados: {e}")
