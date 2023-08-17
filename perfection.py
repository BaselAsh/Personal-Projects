"""
This Is My Module
Basel Did It Alone
This Is My First Program Using Pylint
I Want To Be Great
"""


import random



def random_integer(start: int = 0, end: int = 10) -> int:
    """This Function Returns A Random Number From 'Start' To 'End'"""
    return random.randint(start, end)


def main():
    """This Function Is The Main Funciton"""
    print(random_integer(10, 100))



if __name__ == "__main__":
    main()
