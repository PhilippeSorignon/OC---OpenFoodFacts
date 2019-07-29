import pymysql
import settings

class Database:
    """Everything needed for the Database"""

    def __init__(self):
        self.database_server_ip = "localhost"
        self.database_user_name = settings.USER_NAME
        self.database_user_password = settings.PASSWORD
        self.database_name = "OpenFoodFacts"
        self.char_set = "utf8mb4"
        self.cusror_type = pymysql.cursors.DictCursor


    def create_database(self):
        """Create the database"""
        connection_instance = pymysql.connect(host=self.database_server_ip, \
        user=self.database_user_name, password=self.database_user_password, \
        charset=self.char_set, cursorclass=self.cusror_type)

        try:
            cursor_instance = connection_instance.cursor()
            sql_statement = "CREATE DATABASE IF NOT EXISTS "+self.database_name
            cursor_instance.execute(sql_statement)

        except Exception as e:
            print("Exeception occured:{}".format(e))

        finally:
            connection_instance.close()

    def create_tables(self):
        """Create all the tables"""
        connection_instance = pymysql.connect(host=self.database_server_ip, \
        user=self.database_user_name, password=self.database_user_password, \
        db=self.database_name, \
        charset=self.char_set, cursorclass=self.cusror_type)

        try:
            cursor_instance = connection_instance.cursor()
            sql_statement = "CREATE TABLE IF NOT EXISTS Product(id int PRIMARY KEY AUTO_INCREMENT, name varchar(255), nutri_score char, url varchar(255), saved bool)"
            cursor_instance.execute(sql_statement)

            sql_statement = "CREATE TABLE IF NOT EXISTS AssociationProductStore(product int, store int)"
            cursor_instance.execute(sql_statement)

            sql_statement = "CREATE TABLE IF NOT EXISTS Store(id int PRIMARY KEY AUTO_INCREMENT, name varchar(255))"
            cursor_instance.execute(sql_statement)

        except Exception as e:
            print("Exeception occured:{}".format(e))

        finally:
            connection_instance.close()
