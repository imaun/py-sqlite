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

    def __init__(self, connection, tableName=None):
        self._connection = connection
        self._cursor = connection.cursor()
        self.tableName = tableName

    def setConnection(self, connection):
        self._connection = connection

    def withColumns(self, *columns):
        self._columns = columns

    def createTable(self, tableName=None):
        tbl = tableName
        if tbl is None:
            tbl = self.tableName

        script = f'CREATE TABLE {tbl} ('
        for i in range(len(self._columns)):
            script += self._columns[i]
            if i != len(self._columns) - 1:
                script += ', '
        script += ' );'
        self._connection.execute(script)

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

    def insert(self, *data):
        self.insert_data = data

    def into(self, *columns, tableName=None):
        if tableName is None:
            tableName = self.tableName

        script = f'INSERT INTO {tableName} ('
        for i in range(len(columns)):
            script += columns[i]
            if i != len(columns)-1:
                script += ', '
        script += ') '
        for data in range(len(self.insert_data)):
            script += self.insert_data[data]
            if data != len(columns)-1:
                script += ', '
        script += ')'

        self._connection.execute(script)
