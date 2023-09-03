import sqlite3
from dataclasses import dataclass

class Database:
    def __init__(self, db_name):
        self.db_name = db_name + '.db'
        self.conn = sqlite3.connect(db_name + '.db')
        self.conn.execute('CREATE TABLE IF NOT EXISTS note (id INTEGER PRIMARY KEY, title TEXT, content TEXT NOT NULL);')

    def add(self, note):
        insert = 'INSERT INTO note (title, content) VALUES (?, ?)'
        values = (note.title, note.content)
        self.conn.execute(insert, values)
        self.conn.commit()
    
    def get_all(self):
        select = 'SELECT id, title, content FROM note'
        cursor = self.conn.execute(select)
        lista = []
        for linha in cursor:
            id = linha[0]
            title = linha[1]
            content = linha[2]
            lista.append(Note(id, title, content))
        return lista
    
    def update(self, entry):
        update = 'UPDATE note SET title = ?, content = ? WHERE id = ?'
        values = (entry.title, entry.content, entry.id)
        self.conn.execute(update, values)
        self.conn.commit()
    
    def delete(self, note_id):
        delete = 'DELETE FROM note WHERE id = ?'
        values = (note_id,)
        self.conn.execute(delete, values)
        self.conn.commit()
    def get(self, index):
        cursor = self.conn.execute(
            "SELECT id, title, content FROM note")
        
        for linha in cursor:
            id = linha[0]
            title = linha[1]
            content = linha[2]
            if id == index:
                return Note(id=id, title=title, content=content)
        return None
    
@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''

    
