class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        # new_node.data=data
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top:
            data = self.top.data
            self.top = self.top.next
            return data

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        # new_node.data=data
        if not self.front:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front:
            data = self.front.data
            self.front = self.front.next
            if not self.front:
                self.rear = None
            return data

def is_palindrome(word):
    stack = Stack()
    queue = Queue()
    uniform = ''.join(char.lower() for char in word if char.isalnum())
    for char in uniform:
        stack.push(char)
        queue.enqueue(char)
    for _ in uniform:
        if stack.pop() != queue.dequeue():
            return False

    return True

word = input("Enter a word: ")

if is_palindrome(word):
    print(f"The word {word} is a palindrome.")
else:
    print(f"The word {word} is not a palindrome.")