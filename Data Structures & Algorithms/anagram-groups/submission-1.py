class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_maps = []
        anagrams = []
        for i in range(len(strs)):
            curr = {}
            for j in range(len(strs[i])):
                if strs[i][j] in curr:
                    curr[strs[i][j]] += 1
                else:
                    curr[strs[i][j]] = 1
            if curr in anagram_maps:
                anagrams[anagram_maps.index(curr)].append(strs[i])
            else:
                anagrams.append([strs[i]])
                anagram_maps.append(curr)
        return anagrams
        