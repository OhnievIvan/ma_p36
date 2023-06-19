import sqlite3
 
class define_table:    #інкапсулює функціональність define_table
    def __init__(self, db_name):   #db_name представляє собою ім'я або шлях до файлу бази даних SQLite
        self.conn = sqlite3.connect(db_name)  #встановлює з'єднання з базою даних SQLite, створюється об'єкт з'єднання db_name
        self.cursor = self.conn.cursor()  #Об'єкт курсору дозволяє виконувати SQL-оператори та отримувати результати запитіd
        
    def create_table(self, table_name, columns): #
        columns_str = ', '.join(columns) #об'єднує назви стовпців і типи даних зі списку стовпців у рядок, розділений комами
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_str})"#формування SQL-запит для створення таблицi
        self.cursor.execute(create_table_query) #виконує SQL-запит(створення). дійсний об'єкт курсору для виконання операторів SQL
        self.conn.commit()

    def find_by_key(self, table_name, key): #self (представляє екземпляр класу SimpleORM)
        find_query = f"SELECT * FROM {table_name} WHERE id = ?" #конструює SQL-запит на вибірку всіх стовпців (*) з вказаного table_name і застосовує умову за допомогою речення WHERE для фільтрації рядків, де стовпець id дорівнює параметризованому значенню (?
        self.cursor.execute(find_query, (key,)) #Значення параметра key надається у вигляді одноелементного кортежу (key,) методу execute для заміни параметризованого значення (?) у запитi find_query
        result = self.cursor.fetchone()  #повертає перший рядок з результату запиту
        return result  #Якщо не знайдено жодного відповідного рядка, результатом буде None

    def take_all(self, table_name): #отримання всіх рядків з певної таблиці в базі даних SQLite
        take_all_query = f"SELECT * FROM {table_name}" #вибірку всіх стовпців (*) з вказаного імені таблиці
        self.cursor.execute(take_all_query) #надсилає запит до рушія бази даних для виконання
        result = self.cursor.fetchall() #отримує всі рядки, повернуті запитом, у вигляді списку кортежі
        return result

    def insert(self, table_name, data): #data (словник, що представляє назви стовпців і відповідні їм значення для нового рядка)
        columns = ', '.join(data.keys()) #об'єднує ключі словника даних(представляють назви стовпців)у рядок, розділений комами
        placeholders = ', '.join(['?' for _ in data]) #створює рядок заповнювачів (?)id, для кожного стовпця у словнику даниx
        values = tuple(data.values()) #отримує значення зі словника даних і перетворює їх у кортеж
        
        #SQL-запит для вставки нового рядка в таблицю (заповнювачі)
        insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        self.cursor.execute(insert_query, values) #замінює пропуски (?) у запиті відповідними значеннями з кортежу values
        self.conn.commit()  #гарантує, що вставлений рядок буде постійно зберігатися в базі даних

    def update(self, table_name, key, data): #cтворює рядок присвоєнь стовпців у форматі column = ? 
        set_values = ', '.join([f"{column} = ?" for column in data.keys()]) #для кожного стовпця у словнику даних
        values = tuple(data.values()) #отримує нові значення зі словника даних і перетворює їх у кортеж.
        
        #f-рядок поєднує ім'я_таблиці, set_values та умову для визначення рядка
        update_query = f"UPDATE {table_name} SET {set_values} WHERE id = ?"
        self.cursor.execute(update_query, values + (key,)) #execute замінює заповнювачі (?) у запиті відповідними значеннями з кортежу values. key додається, щоб вказати рядок, який потрібно оновити на основі стовпця id.
        self.conn.commit()

    def delete(self, table_name, key):
        delete_query = f"DELETE FROM {table_name} WHERE id = ?" #SQL-запит на видалення рядка з вказаного імені_таблиц
        self.cursor.execute(delete_query, (key,)) #одноелементного кортежу (key,)
        self.conn.commit()
        
    def close(self):
        self.cursor.close()
        self.conn.close()


db = define_table("hw74.db")

db.create_table("users", ["id INTEGER PRIMARY KEY", "name TEXT", "age INTEGER"])

db.insert("users", {"name": "kate", "age": 35})

db.update("users", 1, {"age": 46})

result = db.find_by_key("users", 1)
print(result)  

all_data = db.take_all("users")
print(all_data)  

db.delete("users", 2)
db.close()