from config import config
import psycopg2
from classes.log import Log


class DbOperations():
    def __init__(self, conn):
        self.conn = conn
        self.new_status = config().get('local_settings','new_status')

    def check_records(self, data):
        cursor = self.conn.cursor()
        number = data[0]
        sql = "SELECT number, status FROM product_motion where number='"+number+"'"
        cursor.execute(sql)
        rows = cursor.fetchall()
        return rows

    def update_record(self, data):
        sql = "UPDATE product_motion SET status='{1}' where number='{0}'".format(data[0][0], self.new_status)
        updated_row = 0
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            updated_row = cursor.rowcount
            Log().save_to_logfile("Update rekordu: {} na status: {}".format(data[0][0], self.new_status))
        except (Exception, psycopg2.DatabaseError) as error:
            print error

        return updated_row
