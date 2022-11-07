# package samples

# Python program to demonstrate stack implementation using a linked list.

# Class representing one position in the stack; only used internally
class Stack:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    # Initializing a stack.
    def __init__(self):
        self.head = None  # Node("head")
        self.size = 0

    # String representation of the stack, for printouts
    def __str__(self):
        cur = self.head
        out = ""
        while cur is not None:
            out += str(cur.value) + "->"
            cur = cur.next
        return "[ " + out[:-2] + " ]"

    # Get the current size of the stack
    def get_size(self):
        return self.size

    # Check if the stack is empty
    def is_empty(self):
        return self.size == 0

    # Get the top item of the stack, without removing it
    def peek(self):
        if self.is_empty():
            raise ValueError("Peeking from an empty stack")
        return self.head.value

    # Push a value onto the stack
    def push(self, value):
        new_node = Stack.Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    # Remove a value from the stack and return it
    def pop(self):
        if self.is_empty():
            raise ValueError("Popping from an empty stack")
        node_to_pop = self.head
        self.head = self.head.next
        self.size -= 1
        return node_to_pop.value

    # Remove all elements from the stack
    def clear(self):
        self.head = None
        self.size = 0


def test():
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)
    print(f"Stack: {stack}")
    for _ in range(1, 6):
        remove = stack.pop()
        print(f"Pop: {remove}")
    print(f"Stack: {stack}")


# Driver Code
if __name__ == "__main__":
    test()
