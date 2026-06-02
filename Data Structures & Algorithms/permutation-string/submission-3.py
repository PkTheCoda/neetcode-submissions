from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        for right in range(len(s2)):

            while (right - left + 1 > len(s1)):
                # if window is larger than len s1, shorten the window, left increment
                left += 1
            
            if (right - left + 1) == len(s1):
                print(s2[left:right + 1])
                if Counter(s1) == Counter(s2[left:right + 1]):
                    return True

        return False

        