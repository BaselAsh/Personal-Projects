"""
This is an implementation of the stack data structure
This project started in 19/6/2023
This project ended in 21/6/2023
"""
# (DONE) TODO remove the None that's in the last element of the list


class Stack:
    """
    This is a stack data structure
    """
    head = None
    def __init__(self, first=None):
        """
        This is the init method
        """
        stack = [first]
        self.stack = stack

    def none(self):
        """
        This method removes the first element if it's value is None
        """
        if len(self.stack) > 1 and self.stack[-1] is None:
            self.stack.pop()

    def push(self, data):
        """
        This method adds data to the head of the stack
        """
        self.stack.insert(0, data)
        Stack.head = self.stack[0]
        self.none()

    def pop(self) -> any:
        """
        This method remove the last element in the stack and returns it's value
        """
        popped_value = self.stack.pop(0)
        Stack.head = self.stack[0]
        self.none()
        return popped_value

    def size(self):
        """
        This method returns the length of the stack
        """
        return len(self.stack)



def main():
    """
    This is the main function.
    It's for testing the stack
    """
    stack = Stack()
    stack.push(3)
    stack.push(20)
    stack.push(11)
    stack.push(35)
    stack.push(23)
    stack.pop()
    stack.pop()
    stack.pop()
    print(stack.head)
    print(stack.size())
    print(stack.stack[-1])


if __name__ == "__main__":
    main()
