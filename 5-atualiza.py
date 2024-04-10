import sqlite3
# 1- Conectando no BD
conexao = sqlite3.connect('brasileirão2023.db')
cursor = conexao.cursor()

# 2-Atualização
posição = 4
cursor.execute(
    """
    UPDATE Brasileirão set time = ?
    WHERE posição = ?
    """,
    ("Bragantino", posição)
    
)
conexao.commit()