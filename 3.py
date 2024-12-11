def is_balanced(string):
    # Initialize an empty stack
    stack = []
    # Traverse the string
    for char in string:
        if char == '(':
            stack.append(char)  # Push opening parenthesis onto the stack
        elif char == ')':
            if not stack:  # Check for unmatched closing parenthesis
                return False
            stack.pop()  # Match found, pop from the stack

    # Check if stack is empty at the end
    return len(stack) == 0

print(is_balanced("()"))
print(is_balanced("("))
