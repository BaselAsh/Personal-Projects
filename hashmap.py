"""
This is Basel Ashraf pure implementation of the hashmap
This file was created in 21/6/2023
The last update was in 21/6/2023
"""


class HashMap:
    """
    - This is the my implementation of the hashmap
    """
    def __init__(self):
        # initialize the size threshold and hash table
        self.size = 8
        self.threshold = .50
        self.table = [None for _ in range(self.size)]

    def insert(self, key, value):
        """
        - This method inserts the key and value pair into the hashed index

        - Takes key, value as Params
        """
        prop_value = 0
        state = True
        count = 0
        while state:
            # Get the hashed index
            index = HashMap._hashit(self, key, prop_value)
            # Check if the index is empty
            if self.table[index] is None:
                self.table[index] = [key, value]
                state = False
            else:
                # Check if the index key matches the key to just change the value
                if self.table[index][0] == key:
                    self.table[index][1] = value
                    state = False
                else:
                    prop_value += 1
        # Check if the table reached the threshold or not
        for i in self.table:
            if i is not None:
                count += 1
        if count >= self.size * self.threshold:
            HashMap._resize(self)

    def remove(self, key):
        """
        - This method removes the key, value pair at the hashed value of key

        - Takes key as Params 
        """
        state = True
        prop_value = 0
        table = self.table
        while state:
            # Get the index of the key by hashing it
            index = HashMap._hashit(self, key, prop_value)
            if table[index][0] == key:
                table[index] = None
                state = False
            else:
                prop_value += 1
        self.table = table

    def _hashit(self, key, prop):
        """
        - This private method returns the hashed value of the key 
        
        - Takes key and prop as Params
        """
        return ((key) + (prop ** 2)) % self.size

    def gettable(self):
        """
        - This method returns the hash table

        - No Params
        """
        return self.table

    def getsize(self):
        """
        - This method returns the size of the hash table

        - No Params
        """
        return self.size

    def _resize(self):
        """
        - This private method resizes the hash table
        """
        # Setting the new size
        self.size *= 2
        # Setting the new table
        new_table = [None for _ in range(self.size)]
        # Getting the index and the pair from the old table to put them in the new table
        for i, pair in enumerate(self.table):
            state = True
            if i is not None:
                while state:
                    prop_value = 0
                    index = HashMap._hashit(self, i, prop_value)
                    if new_table[index] is None:
                        new_table[index] = pair
                        state = False
                    else:
                        prop_value += 1
        self.table = new_table


def main():
    """
    - This is the main function for testing
    """
    ht = HashMap()
    ht.insert(0, 5)
    ht.insert(1, 10)
    ht.insert(2, 20)
    ht.insert(3, 30)
    print(ht.gettable())
    ht.insert(4, 40)
    ht.insert(5, 50)
    ht.insert(6, 60)
    print(ht.gettable())
    ht.insert(6, 65)
    ht.insert(7, 70)
    print(ht.gettable())
    ht.insert(8, 80)
    ht.remove(6)
    ht.insert(9, 90)
    ht.insert(10, 100)
    print(ht.gettable())
    ht.insert(11, 110)
    ht.insert(12, 120)
    print(ht.gettable())
    print(ht.getsize())

if __name__ == "__main__":
    main()
