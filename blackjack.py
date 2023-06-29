"""
This program was started by Basel Ashraf
This program was started at 23/6/2023
This program was finished in ...

- This game when you reach 21 you win
- Or when you reach over 21 you Bust (Lose)
- Or when you get higher than the dealer and lower than the limit (21) you win
- You can stand (not ask for another card)
- Or hit (ask for another card in an attempt to get closer to a count of 21, or even hit 21 exactly)
- It can be between 1 and 9 players
"""
# TODO seperate the main function into small functions
# TODO add the bet and balance and 1.5 times bet if blackjack


import random


class Dealer:
    """
    - This class is the parent class to Player class
    """
    def __init__(self) -> None:
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        self.count = self.deal() + self.deal()

    def deal(self) -> int:
        """
        - This function is for returning a random card number
        """
        return random.choice(self.deck)

    def hit(self) -> None:
        """
        - This function add a card number to the total
        """
        self.count = self.count + self.deal()

    def get_count(self) -> int:
        """
        - This function returns the total
        """
        return self.count


class Player(Dealer):
    """
    - This class inherits from the Dealer class

    Params bet: int, balance: int
    """
    def __init__(self, bet: int=0, balance: int=0) -> None:
        super().__init__()
        self.bet = bet
        self.balance = balance

    def check_bet(self):
        """
        - This method returns True if the bet is less than the balance
        """
        return self.bet <= self.balance


def check_count(count: int) -> bool:
    """
    - This function returns true if the count param equals 21
    - And returns false if the count param is greater than 21
    - And returns none if the count param is less than 21
    """
    if count > 21:
        return False
    if count == 21:
        return True
    if count < 21:
        return None


def blackjack() -> None:
    """
    - This is the main function for implementing the logic of the game
    """
    dealer = Dealer()
    player_one = Player()
    print(f"Dealer numbers are {dealer.getcount()}")
    while True:
        dealer_num = dealer.getcount()
        player_num = player_one.getcount()
        if check_count(player_num) and not checkcount(dealer_num:
            print("BLACKJACK!!! :>")
            print("YOU WIN!!!")
            print("")
            break
        if player_num == 21 and dealer_num == 21:
            print("TIE")
            break
        print(f"Player numbers are {player_num}")
        user_input = input("Hit (h) or Stand (s)?: ").strip().lower()
        if user_input == 'h':
            player_one.hit()
            player_num = player_one.getcount()
            check = checkcount(player_num)
            if check is False:
                print(f"Your Losing Number Is {player_num}")
                print("You Lose")
                break
            if check:
                print("YOU WIN")
                break
            else:
                continue
        elif user_input == 's':
            print(f"You Stand At {player_num}")
            while True:
                dealer_num = dealer.getcount()
                player_num = player_one.getcount()
                check = checkcount(dealer_num)
                if check is False:
                    print(f"Dealer Number Is {dealer_num}")
                    print("YOU WIN")
                    break
                if check:
                    print("YOU LOSE")
                    print(f"Dealer Number Is {dealer_num}")
                    break
                if dealer_num > player_num and dealer_num <= 21:
                    print("YOU LOSE")
                    print(f"Dealer Number Is {dealer_num}")
                    break
                dealer.hit()
                continue
            break
        else:
            print("WRONG INPUT")

if __name__ == "__main__":
    blackjack()
