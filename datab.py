"""
This Program Is The Start Of Learning Data Base
Basel Ashraf Made This App In 4/6/2023 When He Was 16
"""

import sqlite3

def main():
    """This Is The Main Function"""
    # Create Data Base
    db = sqlite3.connect("app.db")


    # Setting Up The Cursor
    cr = db.cursor()

    # Create Tables
    cr.execute("create table if not exists users (user_id INTEGER, name TEXT, skill TEXT, age INTEGER)")
    cr.execute("create table if not exists skills (name TEXT, progress INTEGER, user_id INTEGER)")

    # Insetring Data
    # cr.execute("insert into users(user_id, name) values(1, 'Basel')")
    # cr.execute("insert into users(user_id, name) values(2, 'Omar')")
    # cr.execute("insert into users(user_id, name) values(3, 'Osama')")

    # The Lines From 25 - 34 Is For Adding In Database
    # names_list = ["Ahmed", "Sayed", "Mahmoud", "Ali", "Kamel", "Ibrahim", "Sameh", "Enas"]
    # skills_list = ["Python", "Html", "Css", "Java", "PHP", "Javascript", "C++", "Golang"]
    # ages_list = [15, 23, 54, 43, 21, 18, 16, 42]

    # for key, user in enumerate(names_list):
    #     cr.execute(
    #         f"insert into users(user_id, name, skill, age) values({key + 1}, '{user}', '{skills_list[key]}', {ages_list[key]})")


    # Fetch Data
    cr.execute("select * from users")
    result = cr.fetchall()

    print("<=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=>")
    for row in result:
        print(f"Index -> {row[0]}\nName -> {row[1]}\nSkill -> {row[2]}\nAge -> {row[3]}")
        print("<=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=>")

    # Save (Commit) Changes
    db.commit()

    # Close Data Base
    db.close()


if __name__ == "__main__":
    main()
