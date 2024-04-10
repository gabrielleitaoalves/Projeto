import sqlite3
# 1- Conectando no BD
conexao = sqlite3.connect('brasileirão2023.db')
cursor = conexao.cursor()

# 2 - Leitura de Dados
dados = cursor.execute(
    "SELECT * FROM Brasileirão"
)
print(dados.fetchall())