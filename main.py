import sqlite3
conn = sqlite3.connect('users')
cursor = conn.cursor()
cursor.execute("""create table if not exists users( id integer primary key, name text, email text)""")
conn.commit()

def insert(id, name, email):
    cursor = conn.cursor()
    cursor.execute("""insert into users  (id, name, email) values (:id,:name,:email) """,
                   {"id": id, "name": name, "email": email})
    conn.commit()

def select():
    cursor = conn.cursor()
    cursor.execute("""select * from users""")
    print(cursor.fetchall())

def select_user(id):
    cursor = conn.cursor()
    cursor.execute("""select * from users where id=:id""", {"id": id})
    print(cursor.fetchall())

def delete_user(id):
    cursor = conn.cursor()
    cursor.execute("""delete from users where id=:id""", {"id": id})
    print(cursor.fetchall())
    conn.commit()


def main():
    #insert(1, 'Всеволк', 'wolk@ngs.ru')
    #insert(2, 'Алексей', 'alex@ngs.ru')
    #insert(3, 'Сергей', 'sergo@mail.ru')
    #insert(4, 'Никита', 'neKit@mail.ru')

    select()


main()
conn.close()

