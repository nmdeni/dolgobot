import psycopg2
from colorama import Fore
from config import host,user_name,user_password,db_name

def main(password):
    print()
    try:
        # ОБРАЩЕНИЕ К БД
        connect = psycopg2.connect(f"dbname={db_name} user={user_name} password={password} host={host}")
        cur = connect.cursor()
        cur.execute("select * from users_dolg;")
        # ВЫВОД ДАННЫХ
        for k in cur.fetchall():
            if k[3] == True:
                print(Fore.RED + f"{k[0]} {k[1]} {k[2]}₽")
            else:
                print(Fore.GREEN + f"{k[0]} {k[1]} {k[2]}₽")
            print("_"*20)
            print()
    except:
        return print('[INFO] Ошибка в работе программы!!!')
    finally:
        # ЗАВЕРШЕНИЕ ПРОГРАММЫ
        return print(Fore.WHITE +'[INFO] Завершение!')

# ОБРАБОТКА ПАРОЛЯ
def password_check():
    password_input = input('Введите пароль -> ')

    if  password_input == user_password:
        return main(password_input)
    else:
        return password_check()

# НАЧАЛО
password_check()    