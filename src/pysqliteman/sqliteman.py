import sqlite3


class SQLiteman:

    def __int__(self, db_name):
        self._connection = None
        self._db_name = db_name
        self._cursor = None

    def connect(self, db_name, timeout):
        try:
            self._connection = sqlite3.connect(db_name, timeout)
            self._cursor = self._connection.cursor()
        except sqlite3.Error as e:
            print(e)

    def select(self, table, columns, limit=None):
        query = 'SELECT {0} FROM {1}'.format(columns, table)
        if limit:
            query = query + f' LIMIT {limit}'

        self._cursor.execute(query)
        result = self._cursor.fetchall()
        return result

    def selectAll(self, table, limit=None):
        query = f'SELECT * FROM {table}'
        if limit:
            query = f'{query} LIMIT {limit}'

        self._cursor.execute(query)
        result = self._cursor.fetchall()
        return result

    
