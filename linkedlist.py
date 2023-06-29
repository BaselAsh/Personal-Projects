"""
    This is an implementation of the linkedlist data structure
    This project started in 19/6/2023
    This project ended in
"""


class Node:
    def __init__(self, data=None, after=None):
        self.data = data
        self.after = after

    def getnode(self):
        return self.data

    def setdata(self, data):
        self.data = data


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __len__(self):
        if not self.head:
            return 0
        else:
            count = 0
            node = self.head
            while node:
                node = node.after
                count += 1
            return count

    def __getitem__(self, index):
        return self.head[index]

    def show(self):
        node = self.head
        while node.after:
            print(node.data, end=" -> ")
            node = node.after
        print(node.data)

    def pushfront(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            prev_head = self.head
            self.head = new_node
            new_node.after = prev_head

    def pushback(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.after:
                temp = temp.after
                temp.after = new_node

    def remove(self, index):
        if not self.head:
            return self.head
        else:
            i, size = 1, len(self)
            if index > size:
                index = index % size
            if index == i:
                self.head = self.head.after
                return

            while i < index - 1:
                node = node.after
                i += 1

            if node.after and node.after.after:
                temp = node.after
                node.after = node.after.after
                del temp
            else:
                node.after = None

    def pop(self):
        if not self.head:
            return
        else:
            node = self.head
            prev_node = None
            while node.after:
                prev_node = node
                node = node.after
            prev_node.after = None
            del node

    def reverse(self):
        if not self.head:
            return
        else:
            node = self.head
            prev_node = None
            while node:
                temp = node.after
                node.after = prev_node
                prev_node = node
                node = temp
                if not temp:
                    self.head = prev_node
            return self.head


def main():
    ll = LinkedList()
    ll.pushfront(2)
    ll.pushfront(4)
    ll.pushfront(75)
    ll.pushfront(33)
    ll.show()


if __name__ == "__main__":
    main()
