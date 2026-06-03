from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        t_freq = Counter(t)
        s_freq = {}

        left = 0
        right = 0
        to_return = ""
        
        while right < len(s):
            # add first to s_freq
            s_freq[s[right]] = s_freq.get(s[right], 0) + 1
            is_valid = True

            for key in t_freq:
                if key not in s_freq or t_freq[key] > s_freq[key]:
                    is_valid = False

            # while invalid, push right forward
            if is_valid == False:
                right += 1
            else:
                # while valid, push left forward in hopes of finding shorter string.

                while is_valid == True:
                    if len(s[left:right + 1]) < len(to_return) or to_return == "":
                        to_return = s[left:right + 1]

                    s_freq[s[left]] -= 1
                    if (s_freq[s[left]] <= 0):
                        del s_freq[s[left]] 

                    left += 1
                    for key in t_freq:
                        if key not in s_freq or t_freq[key] > s_freq[key]:
                            is_valid = False

                right += 1

        return to_return
        