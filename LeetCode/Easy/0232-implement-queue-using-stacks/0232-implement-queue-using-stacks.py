class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        reversed_stack = list(reversed(self.stack))
        node = reversed_stack.pop()
        self.stack = list(reversed(reversed_stack))
        return node

    def peek(self) -> int:
        return self.stack[0]
        

    def empty(self) -> bool: 
        return not self.stack
