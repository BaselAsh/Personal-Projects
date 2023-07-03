import random

def main():
    name = get_name()
    print(f"Hello, {name}")


def get_name():
    names = ["Basel", "Ashraf", "Hassan", "Ali", "Hosam", "Omar", "Abdelrhman", "Mohamed"]
    return random.choice(names)


if __name__ == "__main__":
    main()
