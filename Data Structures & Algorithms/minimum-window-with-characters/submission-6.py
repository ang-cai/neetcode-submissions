class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map = {}
        for i in range(len(t)):
            if t[i] in t_map:
                t_map[t[i]] += 1
            else:
                t_map[t[i]] = 1
        l = 0
        r = l
        min_window = ""
        curr = t_map.copy()
        contains = False
        while r < len(s):
            if s[r] in t_map:
                curr[s[r]] -= 1
                contains = True
                for letter in curr:
                    if curr[letter] > 0:
                        contains = False
            while contains and l < len(s):
                if r - l < len(min_window) or min_window == "":
                    min_window = s[l:r+1]
                if s[l] in t_map:
                    curr[s[l]] += 1
                    if curr[s[l]] > 0:
                        contains = False
                l += 1
            r += 1
        while contains and l < len(s):
            if r - l < len(min_window):
                min_window = s[l:r+1]
            if s[l] in t_map and curr[s[l]] < t_map[s[l]]:
                curr[s[l]] += 1
                if curr[s[l]] == t_map[s[l]]:
                    contains = False
            l += 1  
        return min_window     
