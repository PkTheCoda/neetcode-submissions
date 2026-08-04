class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        left = 0
        right = 0
        maxLength = 0
        substring = set()

        while right < len(s):
            while s[right] in substring:
                # invalid
                substring.discard(s[left])
                left += 1
            
            # valid
            substring.add(s[right])
            maxLength = max(maxLength, len(substring))
            right += 1
        
        return maxLength
            

            

