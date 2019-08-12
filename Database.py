import pymysql
import settings

class Database:
    """Everything needed for the Database"""

    def __init__(self):
        """Initialisation"""
        self.database_server_ip = "localhost"
        self.database_user_name = settings.USER_NAME
        self.database_user_password = settings.PASSWORD
        self.database_name = "OpenFoodFacts"
        self.char_set = "utf8mb4"
        self.cusror_type = pymysql.cursors.DictCursor
        self.connection_instance = ""

    def does_database_exists(self):
        """Return if the database exists or not"""
        connection_instance = pymysql.connect(host=self.database_server_ip, \
        user=self.database_user_name, password=self.database_user_password, \
        charset=self.char_set, cursorclass=self.cusror_type)

        try:
            cursor_instance = connection_instance.cursor()
            sql_statement = "SHOW DATABASES"
            cursor_instance.execute(sql_statement)
            result = cursor_instance.fetchall()
            return any(d['Database'] == self.database_name for d in result)



        except Exception as e:
            print("Exeception occured:{}".format(e))

        finally:
            connection_instance.close()

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


    def connect(self):
        """Connection to MariaDB"""
        self.connection_instance = pymysql.connect(host=self.database_server_ip, \
        user=self.database_user_name, password=self.database_user_password, \
        db=self.database_name, \
        charset=self.char_set, cursorclass=self.cusror_type, autocommit=True)


    def disconnect(self):
        """Disconnect from MariaDB"""
        self.connection_instance.close()


    def create_tables(self):
        """Create all the tables"""
        try:
            cursor_instance = self.connection_instance.cursor()
            sql_statement = "CREATE TABLE IF NOT EXISTS\
             Product(id int PRIMARY KEY AUTO_INCREMENT, \
             name varchar(255), category varchar(255), \
             nutri_score char, url varchar(255), saved bool)"
            cursor_instance.execute(sql_statement)

            sql_statement = "CREATE TABLE IF NOT EXISTS \
            AssociationProductStore(product int, store int)"
            cursor_instance.execute(sql_statement)

            sql_statement = "CREATE TABLE IF NOT EXISTS \
            Store(id int PRIMARY KEY AUTO_INCREMENT, name varchar(255))"
            cursor_instance.execute(sql_statement)

        except Exception as e:
            print("Exeception occured:{}".format(e))


    def save_product(self, name, category, nutri_score, url, stores):
        """Save a product in the database"""
        try:
            cursor_instance = self.connection_instance.cursor()
            sql_statement = "INSERT INTO Product (name, category, nutri_score, url, saved)\
             VALUES ('"+name+"', '"+category+"', '"+nutri_score+"', '"+url+"', '0')"
            cursor_instance.execute(sql_statement)

            for current_store in range(len(stores)):
                if not self.does_store_exists(stores[current_store]):
                    self.save_store(stores[current_store])
                self.make_product_store_association(self.get_product_id(name),\
                 self.get_store_id(stores[current_store]))

        except Exception as e:
            print("Exeception occured:{}".format(e))


    def save_store(self, name):
        """Save a store in the database"""
        try:
            cursor_instance = self.connection_instance.cursor()
            sql_statement = "INSERT INTO Store (name) VALUES('"+name+"')"
            cursor_instance.execute(sql_statement)

        except Exception as e:
            print("Exeception occured:{}".format(e))


    def make_product_store_association(self, id_product, id_store):
        """Save a product/store association"""
        try:
            cursor_instance = self.connection_instance.cursor()
            sql_statement = "INSERT INTO AssociationProductStore\
             VALUES('"+str(id_product)+"', '"+str(id_store)+"')"
            cursor_instance.execute(sql_statement)

        except Exception as e:
            print("Exeception occured:{}".format(e))


    def get_products(self, cat):
        """Return a dictionnary of all the products of a certain category saved in the database"""
        result = {}
        try:
            cursor_instance = self.connection_instance.cursor()
            sql_statement = "SELECT * FROM Product WHERE category='"+cat+"'"
            cursor_instance.execute(sql_statement)
            result = cursor_instance.fetchall()

        except Exception as e:
            print("Exeception occured:{}".format(e))

        return result


    def get_saved_products(self):
        """Return a dictionnary of all the saved products"""
        result = {}
        try:
            cursor_instance = self.connection_instance.cursor()
            sql_statement = "SELECT * FROM Product WHERE saved='1'"
            cursor_instance.execute(sql_statement)
            result = cursor_instance.fetchall()

        except Exception as e:
            print("Exeception occured:{}".format(e))

        return result


    def get_product_data(self, name):
        """Return a dictionnary of all the products of a certain category saved in the database"""
        result = {}
        try:
            cursor_instance = self.connection_instance.cursor()
            sql_statement = "SELECT * FROM Product WHERE name='"+name+"'"
            cursor_instance.execute(sql_statement)
            result = cursor_instance.fetchone()

        except Exception as e:
            print("Exeception occured:{}".format(e))

        return result


    def get_stores(self, id_product):
        """Return a dictionnary of all the stores associated to a product"""
        result = {}
        try:
            cursor_instance = self.connection_instance.cursor()
            sql_statement = "SELECT * FROM AssociationProductStore WHERE product='"+id_product+"'"
            cursor_instance.execute(sql_statement)
            result = cursor_instance.fetchall()

        except Exception as e:
            print("Exeception occured:{}".format(e))

        return result


    def product_saved(self, id_product, save):
        """Set a product to saved or not saved"""
        try:
            cursor_instance = self.connection_instance.cursor()
            if save:
                sql_statement = "UPDATE Product SET saved='1' WHERE id='"+id_product+"'"
            else:
                sql_statement = "UPDATE Product SET saved='0' WHERE id='"+id_product+"'"
            cursor_instance.execute(sql_statement)

        except Exception as e:
            print("Exeception occured:{}".format(e))


    def replace_product(self, cat):
        """Return all the product of a given category where the nutri-score is a"""
        score_list = ['a', 'b', 'c', 'd']
        result = ()
        current_score = 0
        while result == ():
            try:
                cursor_instance = self.connection_instance.cursor()
                sql_statement = "SELECT * FROM Product WHERE category='"+cat+"' AND nutri_score='"+score_list[current_score]+"'"
                cursor_instance.execute(sql_statement)
                current_score += 1
                result = cursor_instance.fetchall()

            except Exception as e:
                print("Exeception occured:{}".format(e))

        return result


    def does_store_exists(self, store_name):
        """Check if the store is already saved in the database"""
        try:
            cursor_instance = self.connection_instance.cursor()
            sql_statement = "SELECT * FROM Store WHERE name='"+store_name+"'"
            cursor_instance.execute(sql_statement)
            result = cursor_instance.fetchone()
            return not result is None

        except Exception as e:
            print("Exeception occured:{}".format(e))


    def get_product_id(self, product_name):
        """Return the product ID"""
        try:
            cursor_instance = self.connection_instance.cursor()
            sql_statement = "SELECT id FROM Product WHERE name='"+product_name+"'"
            cursor_instance.execute(sql_statement)
            result = cursor_instance.fetchone()

            return result['id']

        except Exception as e:
            print("Exeception occured:{}".format(e))


    def get_store_id(self, store_name):
        """Return the store ID"""
        try:
            cursor_instance = self.connection_instance.cursor()
            sql_statement = "SELECT id FROM Store WHERE name='"+store_name+"'"
            cursor_instance.execute(sql_statement)
            result = cursor_instance.fetchone()

            return result['id']

        except Exception as e:
            print("Exeception occured:{}".format(e))

    def get_store_name(self, store_id):
        """Return the store name"""
        try:
            cursor_instance = self.connection_instance.cursor()
            sql_statement = "SELECT name FROM Store WHERE id='"+store_id+"'"
            cursor_instance.execute(sql_statement)
            result = cursor_instance.fetchone()

            return result['name']

        except Exception as e:
            print("Exeception occured:{}".format(e))
