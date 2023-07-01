class Warrior():
    def __init__(self):
        self.ranks = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"]
        self.experience = 100
        self.level = 1
        self.rank = self.ranks[self.level//10]
        self.achievements = []
        
    def training(self, inp):
        achive, exp, min_lvl = inp
        if min_lvl > self.level:
            return "Not strong enough"
        self.achievements.append(achive)
        self.increase(exp)
        return achive
        
    def battle(self, lvl):
        if lvl > 100 or lvl < 1:
            return "Invalid level"
        if self.ranks.index(self.ranks[lvl//10]) > self.ranks.index(self.rank) and lvl - self.level >= 5:
            return "You've been defeated"
        if lvl > self.level:
            self.increase(20 * (lvl-self.level) * (lvl-self.level))
            return "An intense fight"
        if lvl == self.level:
            self.increase(10)
            return "A good fight"
        if self.level - lvl == 1:
            self.increase(5)
            return "A good fight"
        if self.level - lvl >= 2:
            return "Easy fight"
            
        
    def increase(self, exp):
        self.experience += exp
        if self.experience > 10000:
            self.experience = 10000
        self.level = self.experience // 100
        self.rank = self.ranks[self.level//10]
        if self.level == 100:
            self.rank = self.ranks[10]
        

if __name__ == "__main__":
    him = Warrior()
    him.increase(8000)
    print(him.experience)
    print(him.level)
    print(him.rank)

"""
1-9 1
10-19 2
20-29 3
30-39 4
40-49 5
50-59 6
60-69 7
70-79 8
80-89 9
90-99 10


"""
