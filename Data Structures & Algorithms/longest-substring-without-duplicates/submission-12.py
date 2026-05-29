class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        maxL = 0
        left = 0

        for right in range(len(s)):

            while s[right] in window:
                window.remove(s[left])
                left += 1
            
            window.add(s[right])
            maxL = max(maxL, len(window))
        
        return maxL
            
        