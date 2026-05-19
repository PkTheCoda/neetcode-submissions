class Solution:

    def encode(self, strs: List[str]) -> str:
        # jump2 play me 
        # 5jump24play2me

        res = ""
        for string in strs:
            created = str(len(string)) + "#" + string
            print(created)
            res += created
        
        print(res)
        return res

    def decode(self, s: str) -> List[str]:

        res = []

        while len(s) != 0:

            len_num = ""
            index = 0
            while s[index] != "#":
                len_num += s[index]
                index += 1


            first_num = int(len_num)
            first_word = s[index + 1:first_num + index + 1]
            res.append(first_word)

            s = s[(index + 1 + first_num):]

        return res
