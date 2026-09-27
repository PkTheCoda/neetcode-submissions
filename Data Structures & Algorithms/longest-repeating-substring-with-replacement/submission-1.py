class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # k represents number of chars we can replace
        # 

        freq = defaultdict(int) # tracks curr window
        left = 0
        right = 0

        max_length = 0
        most_common_count = 0

        while right < len(s):
            freq[s[right]] = freq.get(s[right], 0) + 1
            if freq[s[right]] > most_common_count:
                most_common_count = freq[s[right]]

            right += 1

            # while invalid, not enough replacements
            while ((right - left) - most_common_count) > k:
                freq[s[left]] -= 1
                most_common_count = max(freq.values())
                left += 1
            # while valid, check
            max_length = max(max_length, right - left)
        
        return max_length