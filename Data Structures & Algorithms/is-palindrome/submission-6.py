class Solution:
    def isPalindrome(self, s: str) -> bool:
        total = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] not in total or s[right] not in total:
                if s[left] not in total:
                    left += 1
                if s[right] not in total:
                    right -= 1
            elif s[left].lower() != s[right].lower():
                    return False
            else:
                left += 1
                right -= 1
        
        return True
        