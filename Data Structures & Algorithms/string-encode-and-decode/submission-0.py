class Solution:

    def encode(self, strs: List[str]) -> str:
        coded = ""
        for i in strs:
            code_str = ""
            for j in i:
                code_str += str(ord(j) + 1356)
                code_str += "*"
            coded += code_str
            coded += "$"
        return coded
            

    def decode(self, s: str) -> List[str]:
        decoded = []
        one_str = ""
        for i in s:
            if i != "$":
                one_str += str(i)
            if i == "$":
                char = ""
                string = ""
                for j in one_str:
                    if j == '*':
                        string += chr(int(char) - 1356)
                        char = ""
                    if j != "*":
                        char += j
                decoded.append(string)
                one_str = ""
        return decoded



