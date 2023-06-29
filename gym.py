class Gym:
    complete_volume = 0
    def __init__(self, movement_name, reps, sets) :
        self.movement_name = movement_name
        self.reps = reps
        self.sets = sets
        self.volume = len(self.movement_name) * self.reps * self.sets
        Gym.complete_volume += self.volume
    @classmethod
    def happy(cls) :
        if cls.complete_volume > 500:
            return "Too Much. Lower Your Reps Or Sets Or Both"
        if cls.complete_volume > 250:
            return "Good Job :)"
        if cls.complete_volume < 150:
            return "Work Harder :|"
        else:
            return "Not Bad"
    @staticmethod
    def motivation():
        return "NO PAIN NO GAIN"




def main():
    print(Gym("Deadlift", 4, 200).happy())
    print(Gym.motivation())


if __name__ == "__main__":
    main()
