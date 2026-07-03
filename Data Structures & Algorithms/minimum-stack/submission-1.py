class MinStack:

    def __init__(self):
        self.main_stack = []
        self.assisted_stack = []

    def push(self, val: int) -> None:
        self.main_stack.append(val)
        if not self.assisted_stack or val < self.assisted_stack[-1]:
            self.assisted_stack.append(val)
        else:
            self.assisted_stack.append(self.assisted_stack[-1])
            

    def pop(self) -> None:
        self.main_stack.pop()
        self.assisted_stack.pop()

    def top(self) -> int:
        return self.main_stack[-1]

    def getMin(self) -> int:
        return self.assisted_stack[-1]
        
