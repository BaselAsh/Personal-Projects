# Implement the singleton design pattern in this file
count = 0


class Counter:
    def __init__(self):
        global count
        count += 1

    @staticmethod
    def get_count():
        global count
        return count




if __name__ == "__main__":
    foo = Counter()
    goo = Counter()

    print(count)
