import sqlite3
from faker import Faker
import random

faker = Faker('ru_RU')


def create_db_users(num_users, db_file='users.db'):
    """Скрипт для создания рандомных пользователей"""

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        first_name TEXT,
        last_name TEXT,
        email TEXT,
        password TEXT
    )
    ''')

    for _ in range(num_users):
        first_name = faker.first_name()
        last_name = faker.last_name()
        username = faker.user_name()
        email = faker.email()
        password = faker.password()

        cursor.execute('''
            INSERT INTO users (first_name, last_name, username, email, password)
            VALUES (?, ?, ?, ?, ?)
                       ''', (first_name, last_name, username, email, password))

        conn.commit()
        conn.close()
        print(f"База данных {db_file} создана с {num_users} пользователями!")


create_db_users(50)
