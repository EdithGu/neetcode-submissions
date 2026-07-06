class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = collections.deque()

        for i, token in enumerate(tokens):
            if token not in "+-*/":
                stack.append(int(token))
            else:
                second_place = stack.pop()
                first_place = stack.pop()
                if token == "+":
                    stack.append(first_place + second_place)
                elif token == "-":
                    stack.append(first_place - second_place)
                elif token == "*":
                    stack.append(first_place * second_place)
                elif token == "/":
                    stack.append(int(first_place / second_place))

        return stack[-1]


#  tokens = ["1","2","+","3","*","4","-"]  
#                                         i

#  stack =[5]
    