import sqlite3

# База данных для сотрудников магазина одежды
def add_product():
    try:
        name = input("Введите название товара: ")
        category = input("Введите категорию товара: ")
        price = float(input("Введите цену товара: "))

        conn = sqlite3.connect('clothing_store.db')
        cursor = conn.cursor()
        try:
            cursor.execute("CREATE TABLE products(name, category, price)")
        except:
            cursor.execute('INSERT INTO products (name, category, price) VALUES (?, ?, ?)', (name, category, price))
            conn.commit()
            conn.close()
            print("Товар успешно добавлен")
    except ValueError:
        print("Ошибка: Некорректный формат данных")

def delete_product():
    try:
        name = input("Введите название товара для удаления: ")

        conn = sqlite3.connect('clothing_store.db')
        cursor = conn.cursor()
        try:
            cursor.execute("CREATE TABLE products(name, category, price)")
        except:
            cursor.execute('DELETE FROM products WHERE name = ?', (name,))
            conn.commit()
            conn.close()
            print("Товар успешно удален")
    except ValueError:
        print("Ошибка: Некорректное название товара")

def view_products():
    conn = sqlite3.connect('clothing_store.db')
    cursor = conn.cursor()
    try:
        cursor.execute("CREATE TABLE products(name, category, price)")
    except:
        cursor.execute('SELECT * FROM products')
        products = cursor.fetchall()
        for product in products:
            print(product)
        conn.close()

def add_client():
    try:
        name = input("Введите имя клиента: ")

        conn = sqlite3.connect('clothing_store.db')
        cursor = conn.cursor()
        try:
            cursor.execute("CREATE TABLE clients(name)")
        except:
            cursor.execute('INSERT INTO clients (name) VALUES (?)', (name,))
            conn.commit()
            conn.close()
            print("Клиент успешно добавлен")
    except ValueError:
        print("Ошибка: клиент не был добавлен")

def delete_client():
    try:
        name = input("Введите имя клиента для удаления: ")

        conn = sqlite3.connect('clothing_store.db')
        cursor = conn.cursor()
        try:
            cursor.execute("CREATE TABLE clients(name)")
        except:
            cursor.execute('DELETE FROM clients WHERE name = ?', (name,))
            conn.commit()
            conn.close()
            print("Клиент успешно удален")
    except ValueError:
        print("Ошибка: Некорректный формат имени клиента")

def view_clients():
    conn = sqlite3.connect('clothing_store.db')
    cursor = conn.cursor()
    try:
        cursor.execute("CREATE TABLE clients(name)")
    except:
        cursor.execute('SELECT * FROM clients')
        clients = cursor.fetchall()
        for client in clients:
            print(client)
        conn.close()

def add_shop():
    try:
        name = input("Введите название магазина: ")
        address = input("Введите адресс магазина: ")

        conn = sqlite3.connect('clothing_store.db')
        cursor = conn.cursor()
        try:
            cursor.execute("CREATE TABLE shops(name, address)")
        except:
            cursor.execute('INSERT INTO shops (name, address) VALUES (?, ?)', (name, address))
            conn.commit()
            conn.close()
            print("Магазин успешно добавлен")
    except ValueError:
        print("Ошибка: магазин не был добавлен")

def delete_shop():
    try:
        name = input("Введите название магазина для удаления: ")

        conn = sqlite3.connect('clothing_store.db')
        cursor = conn.cursor()
        try:
            cursor.execute("CREATE TABLE shops(name, address)")
        except:
            cursor.execute('DELETE FROM shops WHERE name = ?', (name,))
            conn.commit()
            conn.close()
            print("Магазин успешно удален")
    except ValueError:
        print("Ошибка: Некорректный формат данных")

def view_shops():
    conn = sqlite3.connect('clothing_store.db')
    cursor = conn.cursor()
    try:
        cursor.execute("CREATE TABLE shops(name, address)")
    except:
        cursor.execute('SELECT * FROM shops')
        shops = cursor.fetchall()
        for shop in shops:
            print(shop)
    conn.close()

def register_user():
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    try:
        cursor.execute("CREATE TABLE users(username, password)")
    except:
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        existing_user = cursor.fetchone()
        if existing_user:
            print("Пользователь с таким именем уже существует")
        else:
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            conn.commit()
            print("Пользователь успешно зарегистрирован")
        conn.close()

def login_user():

    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    try:
        cursor.execute("CREATE TABLE users(username, password)")
    except:
        try:
            cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
            user = cursor.fetchone()
            conn.close()
        except:
            print("Неверный логин или пароль")

        if user:
            print("Вход выполнен успешно")
            while True:
                print("Выберите действие:")
                print("1. Добавить товар")
                print("2. Удалить товар")
                print("3. Посмотреть товары")
                print("4. Добавить клиента")
                print("5. Удалить клиента")
                print("6. Посмотреть клиентов")
                print("7. Добавить магазин")
                print("8. Удалить магазин")
                print("9. Посмотреть магазины")
                print("10. Выйти из аккаунта")

                choice = input("Введите номер действия: ")
                if choice == "1":
                    add_product()
                elif choice == "2":
                    delete_product()
                elif choice == "3":
                    view_products()
                elif choice == "4":
                    add_client()
                elif choice == "5":
                    delete_client()
                elif choice == "6":
                    view_clients()
                elif choice == "7":
                    add_shop()
                elif choice == "8":
                    delete_shop()
                elif choice == "9":
                    view_shops()
                elif choice == "10":
                    break
                else:
                    print("Некорректный выбор. Пожалуйста, введите номер действия от 1 до 10.")
        else:
            print("Неверное имя пользователя или пароль")


while True:
    print("Были у нас раньше?")
    print("1. Регистрация")
    print("2. Авторизация")

    Achoice = input("Введите номер действия: ")
    if Achoice == "1":
        register_user()
    elif Achoice == "2":
        login_user()
    else:
        print("Некорректный выбор. Пожалуйста, введите номер действия 1 или 2.")
