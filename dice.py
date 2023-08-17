"""
This Program Returns Two Random Dices And There Total
I Made This In 3/6/2023 When I Was 16 Years Old
"""


import random


def main():
    """
    This Is The Main Function
    """

    values_list = []
    total_list = []
    times, values_bool, total_bool, rolls = get_inputs()
    for _ in range(times):
        dice_1 = dice_generator()
        dice_2 = dice_generator()
        total = dice_1 + dice_2
        total_list.append(total)
        values_list.append((dice_1, dice_2))
        if rolls:
            print(f"The First Dice: {dice_1}")
            print(f"The Second Dice: {dice_2}")
            print(f"The Total Is {dice_1 + dice_2}")
            print("=--=--=" * 10)
    if values_bool:
        print(values_list)
    if total_bool:
        print(total_list)


def get_inputs():
    while True:
        try:
            times = int(input("How Many Times You Want To Role The Dice?: ").strip())
            break
        except ValueError:
            print("Invalid Input")

    values_bool = input("Do you want to see the list of dices (y|n): ").strip().lower() == "y"
    total_bool = input("Do you want to see the list of totals (y|n): ").strip().lower() == "y"
    rolls = input("Do you want to see the rolls (y|n): ").strip().lower() == "y"
    # TODO return a bool values and total3
    return times, values_bool, total_bool, rolls


def dice_generator():
    """
    This Function Returns A Random Dice Number
    """
    return random.randint(1, 6)


if __name__ == "__main__":
    main()
