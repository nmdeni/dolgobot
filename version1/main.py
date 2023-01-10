from config import users_list

# ОБРАБОТКА/ВЫВОД ДАННЫХ
def main():
    print("\nДобро пожаловать!\n")
    try:
        users = users_list
        for user in users_list:
            for key,val in user.items():
                print(f"{key} -> {val}")

            print("-"*20)
    except:
        return print("[INFO] ошибка данных")
    finally:
        # КОНЕЦ
        return print("Конец программы")

# ВВОД ПАРОЛЯ
def password_check():
    user_password = input("Введите пароль -> ")
    if user_password == "qwerty": # ТУТ ПАРОЛЬ!!!!
        return main()
    else:
        return password_check()
# НАЧАЛО
password_check()