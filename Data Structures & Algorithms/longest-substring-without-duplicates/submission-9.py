class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        window = set()
        max_sub = 0
        l = 0
        r = l
        while r < len(s):
            while r < len(s) and s[r] not in window:
                window.add(s[r])
                r += 1
            max_sub = max(len(window), max_sub)
            if r == len(s):
                return max_sub
            while s[l] != s[r]:
                window.remove(s[l])
                l += 1
            window.remove(s[l])
            l += 1
        return max_sub