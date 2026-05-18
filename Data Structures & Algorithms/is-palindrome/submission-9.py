class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = "abcdefghijklmnopqrstuvwxyz0123456789"
        new_s = ""
        new_s_reversed = ""

        for char in s:
            if char.lower() in valid:
                new_s += char.lower()
        
        new_s_reversed = new_s[::-1]
        return (new_s_reversed == new_s)
