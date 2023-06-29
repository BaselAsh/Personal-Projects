"""
This is for learning regex in python
It's a little easy
"""

import re


def main():
    inp = input("Enter Your Email Address: ")
    the_search = re.search(r"^[A-z0-9_]+(?:\.?[A-z0-9_]+)*@[a-z]+\.com|net|org$", inp)
    if the_search:
        print("Valid")
    else:
        print("Invalid")
    


if __name__ == "__main__":
    main()
