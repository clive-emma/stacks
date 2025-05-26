from collections import deque

def is_palindrome(word):
    # Create a stack and a queue
    stack = []
    queue = deque()

    # Normalize the word to lowercase
    word = word.lower()

    # Fill the stack and queue
    for char in word:
        stack.append(char)
        queue.append(char)

    # Check if the word is a palindrome
    while stack:
        if stack.pop() != queue.popleft():
            return False

    return True

# Example usage
word = input("enter a word")
if is_palindrome(word):
    print(f'"{word}" is a palindrome.')
else:
    print(f'"{word}" is not a palindrome.')
