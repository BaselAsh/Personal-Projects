"""
This Program Is For Training Database
"""
import sqlite3


def main():
    """This Is The Main Function"""
    data_base = sqlite3.connect("app.db")
    cursor = data_base.cursor()
    cursor.execute("insert into users(user_id, name, skill, age) values(5, 'Kamel', 'PHP', 21)")
    cursor.execute("update users set skill = 'C#' where user_id = 5")
    cursor.execute("select * from users")
    results = cursor.fetchall()
    for row in results:
        print(f"user_id -> {row[0]}\nname -> {row[1]}\nskill -> {row[2]}\nage -> {row[3]}")
        print("====-====-====-====-====")

    data_base.commit()
    data_base.close()


if __name__ == "__main__":
    main()

