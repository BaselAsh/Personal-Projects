def main():
    list1 = [1, 2, 3, 4]
    list2 = ["Her", "Him", "Them"]
    tuple1 = ("Python", "Java", "HTML")
    dict1 = {"Name" : "Basel", "Age" : 16, "Country" : "Egypt"}

    zipped = zip(list1, list2, tuple1, dict1)
    for item1, item2, item3, item4 in zipped:
        print(f"list1 item -> {item1}")
        print(f"list2 item -> {item2}")
        print(f"tuple1 item -> {item3}")
        print(f"dict1 key -> {item4}")
        print(f"dict1 value -> {dict1[item4]}")
        



    

if __name__ == "__main__":
    main()