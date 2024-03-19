import sqlite3

from datetime import datetime

# 1)Create sql table with columns: telegram_id , first_name , phone_number,reg_date

# 2)Create sql UserWord with columns: id , telegram_id(PK) , translated_text, date.

# 3)Create functions: registration users , check_user in table User

# 4)Create functions for table UserWord: save_text , delete_text , update_text, get_current_text, get_all_texts

DB = 'data.db'

connection = sqlite3.connect(DB)
sql = connection.cursor()


sql.execute(
    """
    CREATE TABLE IF NOT EXISTS User
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INTEGER,
    first_name TEXT,
    phone_number TEXT,
    reg_date DATETIME);
    """
)


sql.execute(
    """
    CREATE TABLE IF NOT EXISTS UserWord
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    id INTEGER,
    telegram_id INTEGER,
    translated_text TEXT,
    date DATETIME);
    """
)

def register_user(telegram_id, first_name, phone_number):
   connection = sqlite3.connect('data.db')
   sql = connection.cursor()

   sql.execute(" INSERT INTO User (Telegram_ID, First_name, Phone_number, Registered_at) VALUES (?,?,?,?);",
               (telegram_id, first_name, phone_number, datetime.now()))

   connection.commit()
   
def check_user(telegram_id):
    connection = sqlite3.connect('data.db')
    sql = connection.cursor()

    checker = sql.execute(" SELECT telegram_id FROM User WHERE telegram_id = ?; ", (telegram_id,))

    return checker.fetchone()   

def save_text(telegram_id, translated_text, date):
    sql.execute("INSERT INTO UserWord (telegram_id, translated_text, date) VALUES (?, ?, ?)",
                   (telegram_id, translated_text, date))
    connection.commit()


def delete_text(id):
    sql.execute("DELETE FROM UserWord WHERE id = ?", (id,))
    connection.commit()


def update_text(id, new_text):
    sql.execute("UPDATE UserWord SET translated_text = ? WHERE id = ?", (new_text, id))
    connection.commit()


def get_current_text(telegram_id):
    sql.execute("SELECT translated_text FROM UserWord WHERE telegram_id = ? ORDER BY date DESC LIMIT 1", (telegram_id,))
    return get_current_text.fetchone()


def get_all_texts(telegram_id):
    sql.execute("SELECT translated_text FROM UserWord WHERE telegram_id = ?", (telegram_id,))
    return get_all_texts.fetchall()


connection.close()



