"""
- This is the guess the word game
- This game was created by Basel Ashraf
- This game was started in 14/6/2023
- This game was Finished in 15/6/2023
- This game latest update is in 17/6/2023
"""
# TODO Formate the docs of the functions and split the code into small functions as much as possible
# TODO This is after the TODO above count the win rate and the number of games played


import random
from termcolor import colored
import sqlite3


def main():
    """
    This is the main function
    """
    con = sqlite3.connect("namegame.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Info(name TEXT, tries INTEGER)")
    name = get_name()
    tries = 100
    for i in range(1, len(name)+1):
        print(name[:i], end="")
        print("*" * (len(name) - i))
        user_input = get_input()
        if user_input == name.lower():
            print(colored("You Are Correct !!! :)", "green"))
            if i == 1:
                print(colored(f"You Got It In Single Try.", "yellow"))
                tries = i
                break
            print(colored(f"You Got It In {i} Tries.", "yellow"))
            tries = i
            break
        if i == len(name) - 1:
            print(colored("YOU LOST.", "red"))
            print(f"The Name Was: {colored(name, 'yellow')}")
            break
    insert(cur, name, tries)
    average = get_average(cur)
    print(f"Your average is: {colored(average, 'blue')}")
    save_and_close(con)


def get_input():
    """
    Gets input from the user and fix it if needed
    Returns user input
    """
    user_input = input("What is the name?: ").strip().lower()
    user_input = user_input.replace(" ", "")
    return user_input


def get_name():
    """
    Gets random name from all_names.txt file
    Returns random name
    """
    with open("all_names.txt", "r") as myFile:
        names = myFile.readlines()
    name = random.choice(names).strip()
    return name


def insert(cur, name, tries):
    """
    inserts name and tries in the database
    """
    cur.execute("INSERT INTO Info VALUES(?, ?)", (name, tries))
    cur.execute("SELECT tries FROM Info")


def get_average(cur):
    """
    Calculate the average tries for the user
    Returns the average
    """
    all_tries = cur.fetchall()
    average = 0
    for t in all_tries:
        average += t[0]
    average /= len(all_tries)
    the_formation = "{:.3f}".format(average)
    return the_formation


def save_and_close(con):
    """
    Saves and close the database
    """
    con.commit()
    con.close()


if __name__ == "__main__":
    main()
