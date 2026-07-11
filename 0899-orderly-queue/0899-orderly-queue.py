class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        # Case 1: Agar k == 1 hai, toh sirf rotations possible hain
        if k == 1:
            ans = s
            # Saare possible rotations check karo
            for i in range(1, len(s)):
                rotated_str = s[i:] + s[:i]
                if rotated_str < ans:
                    ans = rotated_str
            return ans
            
        # Case 2: Agar k > 1 hai, toh hum string ko poora sort kar sakte hain
        else:
            return "".join(sorted(s))
        