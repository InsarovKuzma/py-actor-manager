import os
import sqlite3

from models import Actor


class ActorManager:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        db_path = os.path.join(base_dir, 'cinema_db.sqlite')
        self.connection = sqlite3.connect(db_path)
        self.table_name = 'actors'

    def create(self, first_name: str, last_name: str):
        self.connection.execute(
            f'INSERT INTO {self.table_name} (first_name, last_name) VALUES (?, ?)',
            (first_name, last_name)
        )
        self.connection.commit()

    def all(self):
        actors_cursor = self.connection.execute(f'SELECT * FROM {self.table_name}')
        return [
            Actor(*row) for row in actors_cursor
        ]

    def update(self, actor_id: int, first_name: str, last_name: str):
        self.connection.execute(
            f'UPDATE {self.table_name} SET first_name = ?, last_name = ? WHERE id = ?',
            (first_name, last_name, actor_id)
        )
        self.connection.commit()

    def delete(self, id_to_delete: int):
        self.connection.execute(f'DELETE FROM {self.table_name} WHERE id = ?',
                                (id_to_delete,))
        self.connection.commit()
