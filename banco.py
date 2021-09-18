import sqlite3

conn = sqlite3.connect('UsuariosBanco.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Usuarios (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Email TEXT NOT NULL,
    Usuario TEXT NOT NULL,
    Senha TEXT NOT NULL

);
""")

print("Conectado ao banco de dados")
