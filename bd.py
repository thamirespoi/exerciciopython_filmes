import sqlite3

# Classe para lidar com o banco de dados
class BD:
    # Construtor
    def __init__(self, banco_dados):
        self.conectarBanco(banco_dados)

    # Conecta no arquivo de banco de dados e cria um cursor
    def conectarBanco(self, banco_dados):
        self.banco = sqlite3.connect(banco_dados)
        self.cursor = self.banco.cursor()

        self.criarTabelaFilmes()

    def criarTabelaFilmes(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS filmes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                genero TEXT NOT NULL,
                duracao TEXT NULL,
                diretor TEXT NULL,
                estudio TEXT NULL,
                classificacao TEXT NULL,
                ano DATE NULL
            )
        """)