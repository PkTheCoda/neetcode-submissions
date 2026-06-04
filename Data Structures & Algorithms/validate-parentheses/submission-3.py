class Solution:
    def isValid(self, s: str) -> bool:
        opening = set("([{")
        closing = set(")]}")

        stack = []

        for char in s:
            if char in opening:
                stack.append(char)
            
            if char in closing:

                if stack and char == ")" and stack[-1] == "(":
                    stack.pop()
                elif stack and char == "}" and stack[-1] == "{":
                    stack.pop()
                elif stack and char == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
        
        if len(stack) != 0:
            return False
        
        return True
                


        