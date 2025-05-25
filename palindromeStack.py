def is_palindrome_stack(s):
    stack = []


    for ch in s:
        stack.append(ch)


    for ch in s:
        if ch != stack.pop():
            return False


# Example usage:
s = input("Enter a word: ").strip()
if is_palindrome_stack(s):
    print(f"The word, {s}, is a palindrome (checked using stack).")
else:
    print(f"The word, {s}, is not a palindrome (checked using stack).")
