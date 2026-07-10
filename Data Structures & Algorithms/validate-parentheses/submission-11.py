class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close = {"{": "}", "[": "]", "(": ")"}
        parenthesis = []
        for i in range(len(s)):
            if s[i] in open_to_close:
                parenthesis.append(s[i])
            else: 
                if len(parenthesis) == 0 or open_to_close[parenthesis[-1]] != s[i]:
                    return False
                parenthesis.pop() 
        return len(parenthesis) == 0
