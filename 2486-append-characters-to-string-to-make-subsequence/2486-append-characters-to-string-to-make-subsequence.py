class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i , j = 0, 0
        n_s, n_t = len(s),len(t)
        while i < n_s and j < n_t:
            if s[i] == t[j]:
                j += 1
            i += 1
        return n_t - j