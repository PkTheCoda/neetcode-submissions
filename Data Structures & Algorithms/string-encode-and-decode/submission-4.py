class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for string in strs:
            str_len = str(len(string))
            encoded = encoded + f"{str_len}-{string}"
        
        print(encoded)
        return encoded


    def decode(self, s: str) -> List[str]:
        strs = []
        right = 0
        while right < len(s):
            built_str_num = ""
            while s[right] != "-":
                built_str_num += s[right]
                right += 1
            
            str_length = int(built_str_num)
            print(str_length)
            print(s[right + 1:right + 1 + str_length])
            strs.append(s[right + 1:right + 1 + str_length])
            right += str_length + 1

        return strs