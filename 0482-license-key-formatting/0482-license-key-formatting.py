class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # 1. Saare dashes hatao aur sabko uppercase banao
        clean = s.replace("-", "").upper()
        
        # 2. String ko reverse karo taaki peeche se k-size ke groups ban sakein
        reversed_clean = clean[::-1]
        
        # 3. Har k characters ka group bana kar list mein daalo
        groups = []
        for i in range(0, len(reversed_clean), k):
            groups.append(reversed_clean[i : i + k])
            
        # 4. Groups ko '-' se jodo aur wapas seedha (reverse) kar do
        return "-".join(groups)[::-1]