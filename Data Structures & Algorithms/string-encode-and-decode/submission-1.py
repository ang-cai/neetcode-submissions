class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for i in range(len(strs)):
            encoded.append(f"{len(strs[i])}.{strs[i]}")
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        left = 0
        right = left
        while right < len(s):
            while s[right].isdigit():
                right += 1
            curr_len = int(s[left:right])
            decoded.append(s[right + 1:right + 1 + curr_len])
            left = right + 1 + curr_len
            right = left
        return decoded