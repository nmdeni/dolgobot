import psycopg2
from config import conf_host,conf_name,conf_password,conf_dbname
from listDb import list_output
# from innerDb import 

def main(host,name,db,password):
    try:
        connect = psycopg2.connect(f'host={host} user={name} dbname={db} password={password}')
        cur = connect.cursor()
        err_type = f"{'-'*20}\n[INFO]Не корректное значение\n{'-'*20}\n"

        # ВХОД В МЕНЮ
        while 1:
            try:
                user_command = int(input("---МЕНЮ---\n1 - вывести список данных\n2 - добавить/удалить данные\n3 - выход\n-> "))

                if user_command == 1:
                    # ВЫВОД СПИСКА
                    list_output(cur)
                    print()
                elif user_command == 2:
                    return print("В РАБОТЕ...")
                elif user_command == 3:
                    break 
                else:
                    print(err_type, 'ошибка')
            except:
                print(err_type)
    except:
        return print(f"{'-'*20}\n[INFO] Ошибка программы!!!\n{'-'*20}\n")
    finally:
        return print("Завершение программы!")

# ОБРАБОТКА ПАРОЛЯ
def password_check():
    user_password = input("Введите пароль -> ")

    if conf_password == user_password:
        return main(conf_host,conf_name,conf_dbname,conf_password)
    else:
        return password_check()

password_check()
