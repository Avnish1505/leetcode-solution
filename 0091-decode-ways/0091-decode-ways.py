class Solution:
    def numDecodings(self, s: str) -> int:
        # Agar string khali hai ya shuruaat mein hi '0' hai, toh decode nahi ho sakta
        if not s or s[0] == '0':
            return 0
            
        n = len(s)
        # p1 represent karta hai dp[i+1] ko, p2 represent karta hai dp[i+2] ko
        # Shuru mein string ke khatam hone ke baad ke base cases:
        p1 = 1  # dp[n] = 1 (ek valid full string decode hone par 1 way)
        p2 = 0  # dp[n+1] = 0
        
        # Peeche se shuru karenge (n-1 se lekar 0 tak)
        for i in range(n - 1, -1, -1):
            current_ways = 0
            
            # 1. Single digit check: Agar 0 nahi hai, toh single digit valid hai
            if s[i] != '0':
                current_ways += p1
                
            # 2. Two digit check: Check karo agar agla character hai aur dono milkar 10-26 banate hain
            if i + 1 < n and (s[i] == '1' or (s[i] == '2' and s[i+1] in '0123456')):
                # Agar i + 2 out of bounds hai (yaani hum bilkul aakhri do chars par hain),
                # toh p2 ki jagah 1 jodenge (kyunki tab ye bhi ek valid complete way banayega)
                current_ways += p2 if i + 2 < n else 1
                
            # Pointers ko shift karo agle iteration ke liye
            p2 = p1
            p1 = current_ways
            
        return p1
        