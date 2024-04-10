import sqlite3
# 1- Conectando no BD
conexao = sqlite3.connect('brasileirão2023.db')
cursor = conexao.cursor()

# 2-Exclusão
id = (1,2)
cursor.execute(
    """
    DELETE FROM Brasileirão
    WHERE posição in (?,?)
    """,
    id
)
conexao.commit()