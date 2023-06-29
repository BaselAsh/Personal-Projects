"""
This Program Returns Two Random Dices And There Total
I Made This In 3/6/2023 When I Was 16 Years Old
"""

import random

def main():
    """This Is The Main Function"""
    values_list = []
    times = int(input("How Many Times Do You Want To Role The Dice? "))
    for _ in range(times):
        dice_1 = dice_generator()
        dice_2 = dice_generator()
        values_list.append((dice_1, dice_2))
        print(f"The First Dice: {dice_1}")
        print(f"The Second Dice: {dice_2}")
        print(f"The Total Is {dice_1 + dice_2}")
    print(values_list)


def dice_generator():
    """This Function Returns A Random Dice Number"""
    return random.randint(1, 6)




if __name__ == "__main__":
    main()
