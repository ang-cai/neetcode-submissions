class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = set()
        for i in range(len(s)):
            if s[i] not in chars:
                chars.add(s[i])
        longest = 0
        for char in chars:
            l = 0
            r = l
            wildcards = 0
            while r < len(s):
                if s[r] == char:
                    r += 1
                elif s[r] != char and wildcards < k:
                    wildcards += 1
                    r += 1
                else:
                    longest = max(longest, r - l)
                    while wildcards == k:
                        if s[l] != char:
                            wildcards -= 1
                        l += 1
            longest = max(longest, r - l)
        return longest
