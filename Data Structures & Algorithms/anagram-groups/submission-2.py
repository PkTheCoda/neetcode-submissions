from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        to_return = []

        for word in strs:
            hashed = tuple(sorted(Counter(word).items())) 

            if hashed in freq:
                freq[hashed].append(word)
            else:
                freq[hashed] = [word]
        
        for key, value in freq.items():
            to_return.append(value)

        return to_return