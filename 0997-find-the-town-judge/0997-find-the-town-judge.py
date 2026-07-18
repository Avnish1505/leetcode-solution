class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # 1 se n tak ke logon ke liye trust scores array (size n + 1)
        trust_scores = [0] * (n + 1)
        
        # Har trust relationship ko process karo
        for a, b in trust:
            trust_scores[a] -= 1  # 'a' trust karta hai, toh score kam karo
            trust_scores[b] += 1  # 'b' par trust kiya gaya, toh score badhao
            
        # Check karo ki kya kisi ka score n - 1 hai
        for i in range(1, n + 1):
            if trust_scores[i] == n - 1:
                return i
                
        return -1