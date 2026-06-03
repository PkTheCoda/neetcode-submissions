from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""
        
        left = 0
        num_in = 0

        t_freq = Counter(t)
        s_freq = {}

        to_return = ""

        for right in range(len(s)):

            # add s_right to s_freq, 0 if doesnt exist
            s_freq[s[right]] = s_freq.get(s[right], 0) + 1
            is_valid = True

            for key in t_freq:
                if key not in s_freq or t_freq[key] > s_freq[key]:
                    is_valid = False
            
            if is_valid:
                while is_valid:
                    if len(s[left:right + 1]) < len(to_return) or to_return == "":
                        to_return = s[left:right + 1]

                    # remove s[left] from s_freq
                    s_freq[s[left]] -= 1
                    
                    if s_freq[s[left]] <= 0:
                        del s_freq[s[left]]
                    
                    left += 1
                    for key in t_freq:
                        if key not in s_freq or t_freq[key] > s_freq[key]:
                            is_valid = False
                    
        return to_return
                    
                    
                    


            # if invalid, just do nothing. itll automatically push right
            
            # if valid, push left until invalid

        