import sqlite3

connection = sqlite3.connect("db_user.sl3", 5)
cur = connection.cursor()

cur.execute("CREATE TABLE IF NOT EXIST Users (id integer primary key autoincrement not null, login TEXT, password TEXT);")

def login():
    print("меню реєстрації")
    log = input("Введіть логін")


connection = sqlite3.connect("db_user.sl3", 5)
connection.comnit()
print("Новий користувач доданий")

if len(res) == 0
    passw = input("Введіть пароль")
cur.execute(f"SELECT * FROM Users WHERE login='{log}', '{passw}')")
connection.comnit()
print("Новий користувач доданий")
else:
print("Такий логін вже існує, спробуйте ще раз")
exit()

def register():
    print("меню реєстрації")
    log = input("Введіть логін")
connection = sqlite3.connect("db_user.sl3", 5)
connection.comnit()
print("Новий користувач доданий")

if len(res) == 0
    passw = input("Введіть пароль")
cur.execute(f"SELECT * FROM Users WHERE login='{log}', '{passw}')")
connection.comnit()
print("Новий користувач доданий")
else:
print("Такий логін вже існує, спробуйте ще раз")
exit()
choise = int(input("1 Увійти\n2. Зареєструватись\n>"))
if choise == 1:
    login()
elif choise == 2:
    register()
else:
    print("Не вірний вибір")
    exit(0)