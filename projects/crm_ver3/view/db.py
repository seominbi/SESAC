import csv
import sqlite3

class crm_database_excutor(object):
    # def __new__(cls, *args, **kwargs):
    #     #유일한 객체 생성
    #     if not hasattr(cls, "_instance"): 
    #         print("__new__ is called\n")
    #         cls.instance = super().__new__(cls)
    #     return cls.instance
    
    def __init__(self):
        #초기화자가 이미 호출된 경우에는 호출 X
        # cls = type(self)
        # if not hasattr(cls, "_init"):
            # print("__init__ is called\n")

            self.conn=sqlite3.connect('database/crm.db',check_same_thread=False)
            self.cursor=self.conn.cursor()

            # cls._init = True
    def get_cursor(self):
        return self.cursor
    
    def get_conn(self):
        return self.conn
    
    def create_table(self):
        self.cursor.execute("""
            drop table user
        """)
        self.cursor.execute("""
            drop table item
        """)
        self.cursor.execute("""
            drop table 'order'
        """)
        self.cursor.execute("""
            drop table orderitem
        """)
        self.cursor.execute("""
            drop table store
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS "user"(
                "id" text primary key, "name" text, 
                "gender" text, "age" text, 
                "birthdate" text, 
                "address" text)
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS "item"(
                "id" text primary key, 
                "name" text, 
                "type" text, 
                "unitPrice" text)
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS "store"(
                "id" text primary key, 
                "name" text, 
                "type" text, 
                "address" text)
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS "order"(
                "id" text primary key, 
                "orderAt" text, 
                "storeId" text, 
                "userId" text, 
                foreign key("storeId") references store("id"), 
                foreign key ("userId") references user(id))
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS "orderitem"(
                "id" text primary key, 
                "orderId" text, 
                "itemId" text, 
                foreign key("orderId") references "order"("id"), 
                foreign key ("itemId") references item(id))
        """)

        self.conn.commit()

    def user_csv_to_db(self):
        with open('database/user.csv','r',newline="", encoding='utf-8') as file:
            csv_reader = csv.reader(file) 
            next(csv_reader)
            tuples = []

            for row in csv_reader:
                tuple_data = tuple(row)
                tuples.append(tuple_data)

            self.cursor.executemany("INSERT INTO user(id, name, gender, age, birthdate, address) VALUES (?, ?, ?, ?, ?, ?)", tuples)

            self.conn.commit()

    def item_csv_to_db(self):
        with open('database/item.csv','r',newline="", encoding='utf-8') as file:
            csv_reader = csv.reader(file) 
            next(csv_reader)
            tuples = []

            for row in csv_reader:
                tuple_data = tuple(row)
                tuples.append(tuple_data)

            self.cursor.executemany("INSERT INTO item(id,name, type, unitPrice) VALUES (?, ?, ?, ?)", tuples)

            self.conn.commit()
    
    def store_csv_to_db(self):
        with open('database/store.csv','r',newline="", encoding='utf-8') as file:
            csv_reader = csv.reader(file) 
            next(csv_reader)
            tuples = []

            for row in csv_reader:
                tuple_data = tuple(row)
                tuples.append(tuple_data)

            self.cursor.executemany("INSERT INTO store(id,name, type, address) VALUES (?, ?, ?, ?)", tuples)

            self.conn.commit()

    def order_csv_to_db(self):
        with open('database/order.csv','r',newline="", encoding='utf-8') as file:
            csv_reader = csv.reader(file) 
            next(csv_reader)
            tuples = []

            for row in csv_reader:
                tuple_data = tuple(row)
                tuples.append(tuple_data)

            self.cursor.executemany("INSERT INTO 'order'(id, orderAt, storeId, userId) VALUES (?, ?, ?, ?)", tuples)

            self.conn.commit()

    def orderitem_csv_to_db(self):
        with open('database/orderitem.csv','r',newline="", encoding='utf-8') as file:
            csv_reader = csv.reader(file) 
            next(csv_reader)
            tuples = []

            for row in csv_reader:
                tuple_data = tuple(row)
                tuples.append(tuple_data)

            self.cursor.executemany("INSERT INTO orderitem(id, orderId, itemId) VALUES (?, ?, ?)", tuples)

            self.conn.commit()



# query="select * from user limit 10"
# cursor.execute(query)
# result=cursor.fetchall()
# print(result)

# conn.commit()
# conn.close()