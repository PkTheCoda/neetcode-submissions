class Solution:
    def isPalindrome(self, s: str) -> bool:

        valid = "abcdefghijklmnopqrstuvwxyz0123456789"

        p1 = 0
        p2 = len(s) - 1

        while (p1 < p2):
            print([p1, s[p1]])
            print([p2, s[p2]])
            if (s[p1].lower() not in valid):
                p1 += 1
            elif (s[p2].lower() not in valid):
                p2 -= 1
            else:
                if (s[p1].lower() != s[p2].lower()):
                    return False
                else:
                    p1 += 1
                    p2 -= 1

        return True
        