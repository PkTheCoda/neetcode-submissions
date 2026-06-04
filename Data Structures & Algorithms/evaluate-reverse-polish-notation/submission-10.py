class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = set("+-*/")
        total = 0
        stack = []
        for i in range(len(tokens)):

            if tokens[i] in ops:
                first_pop = int(stack.pop())
                second_pop = int(stack.pop())
                print(first_pop, second_pop, tokens[i])

                if tokens[i] == "+":
                    stack.append(second_pop + first_pop)
                elif tokens[i] == "-":
                    stack.append(second_pop - first_pop)
                elif tokens[i] == "*":
                    stack.append(second_pop * first_pop)
                elif tokens[i] == "/":
                    stack.append(int(second_pop / first_pop))

            else:
                stack.append(tokens[i])
        
        return int(stack.pop())
        