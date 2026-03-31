from pathlib import Path
import sqlite3

# Define o caminho do banco dentro do container
DB_PATH = Path("/data/lab.db")

def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection

def init_db():
    # Cria a pasta /data se não existir
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    
    with get_connection() as connection:
        # Cria a tabela de projetos [cite: 259]
        connection.execute("""
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                status TEXT NOT NULL
            )
        """)
        
        # Verifica se já existem dados para não duplicar
        count = connection.execute("SELECT COUNT(*) FROM projects").fetchone()[0]
        
        if count == 0:
            # Dados iniciais do laboratório [cite: 271, 272, 274, 275]
            projects = [
                ("Portal da Associação Comunitária", "Comunidade", "Planejamento"),
                ("Painel de Ações da ONG", "ONG", "Preparação"),
                ("Agenda Digital da Escola", "Educação", "Estrutura inicial"),
            ]
            connection.executemany(
                "INSERT INTO projects (name, category, status) VALUES (?, ?, ?)",
                projects
            )
            connection.commit()

def list_projects():
    with get_connection() as connection:
        rows = connection.execute(
            "SELECT id, name, category, status FROM projects ORDER BY id"
        ).fetchall()
        return [dict(row) for row in rows]