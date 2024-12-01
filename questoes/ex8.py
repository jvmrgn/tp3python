import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///INFwebNET_DB.db")

consulta_sql = """
SELECT * 
FROM Usuarios_Historicos
WHERE idade BETWEEN 22 AND 30
"""

usuarios_22_30 = pd.read_sql_query(consulta_sql, con=engine)

print(usuarios_22_30)
