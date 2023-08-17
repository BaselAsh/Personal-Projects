from time import time

def speedTest(func):
    def wrapper():
        start = time()
        func()
        end = time()
        print(f"Function Took {end - start} Seconds")
    return wrapper


@speedTest
def myfunc():
    for i in range(1000):
        print(i)
    


def main():
    myfunc()




if __name__ == "__main__":
    main()