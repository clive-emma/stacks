from collections import deque

class Solution:
    def _init_(self):
        self.stack = []
        self.queue = deque()

    def pushCharacter(self, ch):
        self.stack.append(ch)

    def enqueueCharacter(self, ch):
        self.queue.append(ch)

    def popCharacter(self):
        return self.stack.pop()

    def dequeueCharacter(self):
        return self.queue.popleft()

# Read the input
s = input()

# Create the Solution object
obj = Solution()

# Fill stack and queue with characters
for ch in s:
    obj.pushCharacter(ch)
    obj.enqueueCharacter(ch)

is_palindrome = True

# Compare characters popped from stack and dequeued from queue
for i in range(len(s) // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        is_palindrome = False
        break

# Print result
if is_palindrome:
    print(f"The word, {s}, is a palindrome.")
else:
    print(f"The word, {s}, is not a palindrome.")