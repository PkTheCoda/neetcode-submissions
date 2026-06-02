from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = Counter(s1)
        s2_freq = {}
        left = 0
        for right in range(len(s2)):

            s2_freq[s2[right]] = s2_freq.get(s2[right], 0) + 1

            while (right - left + 1 > len(s1)):
                # if window is larger than len s1, shorten the window, left increment
                # remove left from s2_freq first tho
                s2_freq[s2[left]] -= 1
                if (s2_freq[s2[left]] <= 0):
                    del s2_freq[s2[left]]
                left += 1
            
            if (right - left + 1) == len(s1):
                if s1_freq == s2_freq:
                    return True

        return False

        