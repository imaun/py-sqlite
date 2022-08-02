import sqlite3


class SQLiteman:

    def __int__(self, db_name):
        self._connection = None
        self._db_name = db_name
        self._cursor = None
        self._table = SQLiteTable()

    def connect(self, db_name, timeout):
        try:
            self._connection = sqlite3.connect(db_name, timeout)
            self._cursor = self._connection.cursor()
        except sqlite3.Error as e:
            print(e)

    def getDbName(self):
        return self._db_name;

    def getConnection(self):
        return self._connection


class SQLiteTable:

    def __init__(self, tableName=None):
        self.tableName = tableName

    def setConnection(self, conn):
        self.connection = conn

    def withColumns(self, *columns):
        self.columns = columns

    def createTable(self, tableName=None):
        tbl = tableName
        if tbl is None:
            tbl = self.tableName

        script = f'CREATE TABLE {tbl} ('
        for i in range(len(self.columns)):
            script += self.columns[i]
            if i != len(self.columns) - 1:
                script += ', '
        script += ' );'
        self.connection.execute(script)

    def select(self, table, columns, limit=None):
        if table is None:
            table = self.tableName

        query = 'SELECT {0} FROM {1}'.format(columns, table)
        if limit:
            query = query + f' LIMIT {limit}'

        self._cursor.execute(query)
        result = self._cursor.fetchall()
        return result

    def selectAll(self, table=None, limit=None):
        if table is None:
            table = self.tableName

        query = f'SELECT * FROM {table}'
        if limit:
            query = f'{query} LIMIT {limit}'

        self._cursor.execute(query)
        result = self._cursor.fetchall()
        return result
