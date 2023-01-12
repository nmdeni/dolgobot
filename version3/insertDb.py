def insert_db(db_cursor):
    result_insert = ''

    try:
        user_name = input('Введите ваше имя -> ')
        user_sum = int(input('Введите сумму долга -> '))
        user_status = int(input('Введите чей долг (1-вы 2-вам) -> '))

        if user_status == 1:
            user_status = 'True'
        else:
            user_status = 'False'

        db_cursor.execute(f"""
            insert into users_dolg(user_name,user_sum,user_status) 
            values ('{user_name}',{user_sum},{user_status});
        """)

        result_insert = input(f"{'-'*20}\n[INFO] Данные записаны нажмите ENTER\n{'-'*20}")
    except:
        result_insert = print(f"{'-'*20}\n[INFO] Данные не записаны\n{'-'*20}")
    finally:
        return result_insert