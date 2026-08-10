class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Fast O(1) lookup ke liye dictionary ko set mein convert karo
        word_set = set(wordDict)
        
        # dp[i] store karega ki prefix s[0:i] valid break banata hai ya nahi
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Base case: empty string is valid
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                # Agar pehle j tak ka part valid tha aur bacha hua s[j:i] dictionary mein hai
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # Ek bhi valid split mil gaya toh is i ke liye aage search stop karo
                    
        return dp[len(s)]