class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
        
    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None
    def size(self):
        return len(self.items)
    
    def show(self):
        for char in self.items:
            for digit in char:
                print(digit,end=" ")



stack = Stack()

numbers = ['1','2','3','4','5','6','7','8','9']
operators = ['+', '-', '*', '/']

input = str(input(""))

# Iterate from the end of the prefix number
for char in reversed(input):
    # If char in number from 1 to 9 push into the stack
    if char in numbers:
        stack.push(char)
    # If char is operators, take 1st and 2nd number out of the stack
    # and combine with operator
    elif char in operators:
        first_number = stack.pop()
        second_number = stack.pop()
        result = first_number + second_number + char
        stack.push(result)
    # Skip if char is 0
    elif char == 0:
        input.pop()

# Print the result out
stack.show()

