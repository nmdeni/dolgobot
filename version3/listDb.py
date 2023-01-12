from colorama import Fore

def list_output(db_cursor):
    db_cursor.execute("""
        select * from users_dolg;
    """)
    for k in db_cursor.fetchall():
        if k[3] == True:
            print(Fore.RED + f"{k[0]} {k[1]} {k[2]}₽")
        else:
            print(Fore.GREEN + f"{k[0]} {k[1]} {k[2]}₽")
    return input(Fore.WHITE +"ENTER") 