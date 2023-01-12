def delDateDb(db_cursor):
    result_insert = ''

    try:
        delete_item = int(input('Введите данные для удаления (пример - 1(номер записи))'))

        db_cursor.execute(f"""
            delete from users_dolg where id = {delete_item}
        """)
        
        result_insert = input(f"{'-'*20}\n[INFO] Данные записаны нажмите ENTER\n{'-'*20}")
    except:
        result_insert = print(f"{'-'*20}\n[INFO] Данные не записаны. Ошибка!!!\n{'-'*20}")
    finally:
        return result_insert