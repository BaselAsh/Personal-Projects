"""
This Is The First Trainging On The Database
Started In 5/6/2023
Basel Ashraf Made This Program
"""

import sqlite3




def main():
    """ This Is The Main Function """
    input_message = """
What Do You Want To Do ?
"s" => Show All Skills
"a" => Add New Skill
"d" => Delete A Skill
"u" => Update Skill Progress
"q" => Quit The App
Choose Option: """
    user_input = input(input_message).strip().lower()

    check_input(user_input)

    if user_input == 's':
        show_skills()
    elif user_input == 'a':
        add_skills()
    elif user_input == 'd':
        delete_skills()
    elif user_input == 'u':
        update_skills()
    else:
        input("Type Any Thing To Close The App. \n")



def dec_func(show):
    """ This Is A Docerator Function """
    def another():
        print("=====-----=====-----=====-----=====-----=====")
        show()
        print("=====-----=====-----=====-----=====-----=====")
    return another





def check_input(inp):
    """ This Function Checks If The Input Is Valid """
    inputs = ['s', 'a', 'd', 'u', 'q']
    if inp not in inputs:
        print("This Input Is Not Valid")


@dec_func
def show_skills():
    """ This Function Shows The User All The Skill And Their Progress """
    con = sqlite3.connect("app.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS skills (name TEXT, progress INTEGER, user_id INTEGER)")
    cur.execute("SELECT * FROM skills")
    results = cur.fetchall()
    print("=-=-=-=-=-=-=-=-=-=-=-=-=")
    for row in results:
        print(f"User_ID: {row[2]}")
        print(f"Skill: {row[0]}")
        print(f"Progress: {row[1]}%")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=")
    con.commit()
    con.close()


def add_skills():
    """ This Function Add Skill To The Database"""
    con = sqlite3.connect("app.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS skills (name TEXT, progress INTEGER, user_id INTEGER)")
    new_skill = input("What's Your New Skill: ").strip().capitalize()
    skill_progress = int(input("What's Your New Skill Progress: ").strip())
    user_id = int(input("What's Your User ID: ").strip())
    check_skill = cur.execute(f"SEARCH name FROM skills WHERE user_id = {user_id}")
    if check_skill is None:
        cur.execute("INSERT INTO skills values (?, ?, ?)", (new_skill, skill_progress, user_id))
    print("This SKill Already Exists")
    bol = input("Would You Like To Update This Skill Progress?: ").strip().lower
    if bol == "y":
        update_skills()
    con.commit()
    con.close()


def delete_skills():
    """ This Function Deletes A Skill From The Database"""
    con = sqlite3.connect("app.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS skills (name TEXT, progress INTEGER, user_id INTEGER)")
    skill = input("What Skill Would You Like To Delete: ").strip().capitalize()
    user_id = int(input("What Is Your User ID: ").strip())
    cur.execute(f"DELETE FROM skills WHERE user_id = {user_id} AND name = '{skill}'")
    con.commit()
    con.close()


def update_skills():
    """ This Function Update The Progress Of A Skill In The Database"""
    con = sqlite3.connect("app.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS skills (name TEXT, progress INTEGER, user_id INTEGER)")
    skill = input("Which Skill: ").strip().capitalize()
    new_prog = int(input("Change Progress To What: ").strip())
    user_id = int(input("What's Your User ID: ").strip())
    cur.execute(
        f"UPDATE skills SET progress = {new_prog} WHERE name = '{skill}' AND user_id = {user_id}")
    con.commit()
    con.close()

def save_and_close():
    """ This Function Save The Changes And Close The Database"""
    con = sqlite3.connect("app.db")
    con.commit()
    con.close()



if __name__ == "__main__":
    main()
