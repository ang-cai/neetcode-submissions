class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while right > left:
            while left < len(s) and not s[left].isalnum():
                left += 1
            while right > -1 and not s[right].isalnum():
                right -= 1
            if right > left and s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            elif right > left:
                return False
        return True