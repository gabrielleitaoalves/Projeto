import sqlite3

# 1- Conectando no BD
conexao = sqlite3.connect('brasileirão2023.db')

cursor = conexao.cursor()

# 2-Inserindo Dados
cursor.execute(
    """
        INSERT INTO Brasileirão(time, pontos, vitorias)
        VALUES ('Gremio', 68, 21)
    """
)

cursor.execute(
    """
        INSERT INTO Brasileirão(time, pontos, vitorias)
        VALUES ('Atletico MG', 66, 19)
    """
)

cursor.execute(
    """
        INSERT INTO Brasileirão(time, pontos, vitorias)
        VALUES ('Flamengo Urubu', 66, 19)
    """
)

cursor.execute(
    """
        INSERT INTO Brasileirão(time, pontos, vitorias)
        VALUES ('Botafogo', 64, 18)
    """
)
conexao.commit()
conexao.close()