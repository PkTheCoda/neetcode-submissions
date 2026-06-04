class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force
        
        result = []

        for left in range(len(temperatures)):
            has_temp = False
            for right in range(left, len(temperatures)):

                if temperatures[right] > temperatures[left]:
                    result.append(right - left)
                    has_temp = True
                    break
            
            if not has_temp:
                result.append(0)
        
        return result
                
        