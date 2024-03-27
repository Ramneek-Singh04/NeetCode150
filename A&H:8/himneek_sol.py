class Solution:

    def encode(self, strs: List[str]) -> str:
        new_string = ""
        for word in strs:
            new_string = new_string + "&" + word
        return new_string

    def decode(self, s: str) -> List[str]:
        result = []
        if s == "":
            empty_string = ""
            result.append(empty_string)
        else:
            i = 0
            while i < len(s):
                j = i
                while j < len(s) and s[j] != "&":
                    j += 1
                if i > 0 or j > i:
                    result.append(s[i:j])
                i = j + 1
            
        return result
