class Solution:
    def isValid(self, s: str) -> bool:
        brackets_stack = collections.deque()

        for bracket in s:
            if bracket == '(' or bracket == '[' or bracket == '{':
                brackets_stack.append(bracket)
            else:
                popped_bracket = brackets_stack.pop() if brackets_stack else False
                if bracket == ')':
                    if popped_bracket != '(':
                        return False
                elif bracket == '}':
                    if popped_bracket != "{":
                        return False
                elif bracket == ']':
                    if popped_bracket != '[':
                        return False

        # important back checking!!
        
        return len(brackets_stack) == 0