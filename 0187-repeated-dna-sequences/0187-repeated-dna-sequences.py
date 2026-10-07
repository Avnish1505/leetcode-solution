class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        seen = set()
        repeated = set()

        L = 10
        n = len(s)

        for i in range(n - L + 1):
            sub = s[i : i + L]
            if sub in seen:
                repeated.add(sub)
            else:
                seen.add(sub)
            
        return list(repeated)