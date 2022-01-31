from mysql import connector
from Zalypa.config import Config
from mysql.connector import Error
from abc import ABC

class Model(ABC):
    table = ""
    @classmethod
    def connects(cls):
        try:
            cls.conn = connector.connect(host=Config.host,
                                         port=Config.port,
                                         user=Config.user,
                                         database=Config.database,
                                         password=Config.password)

            if cls.conn.is_connected():
                print('Connected to MySQL database')

        except Error as e:
            print(e)
        cursor = cls.conn.cursor()
        return cursor

    @classmethod
    def get_by_id(cls,id):
        cursor = cls.connects()
        sql = ('SELECT * FROM ' + cls.table + ' WHERE id =' + str(id))
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    @classmethod
    def get_all(cls):
        cursor = cls.connects()
        sql = ('SELECT * FROM ' + cls.table)
        cursor.execure(sql)
        result = cursor.fetchall()
        return result



