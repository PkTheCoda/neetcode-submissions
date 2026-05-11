from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        a = []

        for string in strs:
            if tuple(sorted(Counter(string).items())) in d:
                d[tuple(sorted(Counter(string).items()))].append(string)
            else:
                d[tuple(sorted(Counter(string).items()))] = [string]
        
        for item in d:
            print(item)
            a.append(d[item])
        
        return a
        