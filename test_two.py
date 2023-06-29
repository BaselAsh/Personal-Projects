class HashTable:
    size = 8

    def __init__(self):
        self.hashtable = [None for _ in range(HashTable.size)]

    def insert(self, key, value):
        index = HashTable.hashit(self, key)
        self.hashtable[index] = [key, value]

    @staticmethod
    def hashit(key):
        return (key * 4 // 3) % HashTable.size
    
    def gethashtable(self):
        return self.hashtable


hashtable = HashTable()
hashtable.insert(1, 12)
hashtable.insert(2, 23)
hashtable.insert(3, 44)
hashtable.insert(4, 64)
print(hashtable.gethashtable())
