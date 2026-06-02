class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxL = 0
        left = 0
        freq_char_count = 0
        freq = {}

        for right in range(len(s)):

            if s[right] in freq:
                freq[s[right]] += 1
                freq_char_count = max(freq_char_count, freq[s[right]])
            else:
                freq[s[right]] = 1
                freq_char_count = max(freq_char_count, freq[s[right]])

            # if length of window - most freq char > k, false.
            while ((right - left + 1) - freq_char_count > k):
                # invalid
                freq[s[left]] -= 1
                left += 1

            # valid
            maxL = max(maxL, right - left + 1)
            
        
        return maxL
        