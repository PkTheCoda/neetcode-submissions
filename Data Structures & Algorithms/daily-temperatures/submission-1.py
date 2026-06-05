class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []

        for index in range(len(temperatures)):


            # pop any smaller numbers on stack
            while len(stack) != 0 and temperatures[index] > temperatures[stack[-1]]:
                popped = stack.pop()
                output[popped] = index - popped

            # add to stack
            stack.append(index)
        

        return output

