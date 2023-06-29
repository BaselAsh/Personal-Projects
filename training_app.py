""" This App Was Created By (Basel Ashraf) In 4/6/2023"""

import sqlite3

def main():
    """ This Is The Main Function """
    message = """
    Input Here NOW!
    "s" => Show All Skills
    "a" => Add New Skill
    "d" => Delete A Skill
    "u" => Update A Skill
    "q" => Quit The App
    INPUT HERE NOW: """
    try:
        db = sqlite3.connect("app.db")
        cr = db.cursor()
        user_input = input(message).lower()
        len_db = 0
        if user_input == "s":
            results = cr.execute("select * from user")
            for row in results:
                print(f"Index -> {row[0]}\nSkill -> {row[1]}\n====---====---====")
                len_db += 1
        elif user_input == "a":
            results = cr.execute("select * from user")
            for row in results:
                len_db += 1
            results = cr.execute("select * from user")
            add_input = input("What Do You Want To Add: ")
            cr.execute(f"insert into user(skill_num, skill) values({len_db + 1}, '{add_input}')")
        elif user_input == "d":
            delete_input = int(input("Where Do You Want To Delete: "))
            cr.execute(f"delete from user where skill_num = {delete_input}")
        elif user_input == "u":
            update_input_num = int(input("Where Do You Want To Update: "))
            update_input_what = input("What Is The New Value: ")
            cr.execute(f"update user set skill = '{update_input_what}' where skill_num = {update_input_num}")
        else:
            pass


    except sqlite3.DatabaseError:
        print("There Was An Error")
    finally:
        db.commit()
        db.close()



if __name__ == "__main__":
    main()