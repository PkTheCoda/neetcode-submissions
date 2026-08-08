class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0
        n = len(chars)

        while read < n:
            chars[write] = chars[read] #first element is ALWAYS letter
            write += 1
            j = read + 1
            while j < n and chars[j] == chars[read]:
                j += 1
            
            if j - read > 1:
                for char in str(j - read):
                    chars[write] = char
                    write += 1
            
            read = j

        return write