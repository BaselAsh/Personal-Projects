"""
This Program Generates A Random Card
Basel Ashraf Made This Program In 3/6/2023
"""
import random

def main():
    """This Is The Main Function"""
    print(card_generator())

def card_generator():
    """This Function Returns A Random Card"""
    cards_type = ["Spade", "Diamond", "Clubs", "Hearts"]
    cards_name = [
    "Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Queen", "King", "Jack"
    ]
    random_card_type = random.choice(cards_type)
    random_card_name = random.choice(cards_name)
    return f"{random_card_name} Of {random_card_type}"



if __name__ == "__main__":
    main()
