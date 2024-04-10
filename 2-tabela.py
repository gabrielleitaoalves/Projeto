import sqlite3

# 1- Conectando no BD
conexao = sqlite3.connect('brasileirão2023.db')

cursor = conexao.cursor()

# 2-Criação da Tabela
cursor.execute(
    """
        CREATE TABLE Brasileirão(
          posição INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,  
          time TEXT NOT NULL,
          pontos INTEGER NOT NULL,
          vitorias INTEGER NOT NULL
        );
    """
)
# 3- Fecha conexão
conexao.close()
print("Tabela foi criada")