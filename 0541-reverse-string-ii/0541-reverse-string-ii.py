class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # String ko list mein convert karo for mutability
        chars = list(s)
        n = len(chars)
        
        # Har 2k block par jump karo
        for i in range(0, n, 2 * k):
            # i se lekar (i + k) tak ke elements reverse karo.
            # min(i + k, n) ensure karta hai ki end mein agar k se kam elements hon toh out-of-bounds na ho!
            chars[i : i + k] = chars[i : i + k][::-1]
            
        # List ko wapas string mein join kar do
        return "".join(chars)