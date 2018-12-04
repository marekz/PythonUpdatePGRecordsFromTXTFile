from config import config
import psycopg2


class DbConnect():
    def __init__(self):
        self.host = config().get('db_settings','host')
        self.user = config().get('db_settings','username')
        self.password = config().get('db_settings','password')
        self.port = config().get('db_settings','port')
        self.database = config().get('db_settings','database')

    def conn(self):
        conn = psycopg2.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password
        )

        return conn

