class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        s_set = set()
        right = 0
        left = 0
        max_len = 0

        while right < len(s):
            
            while s[right] in s_set:
                s_set.discard(s[left])
                left += 1
            
            s_set.add(s[right])
            right += 1
            max_len = max(max_len, right - left)
        
        return max_len