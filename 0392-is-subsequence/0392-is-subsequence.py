class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        
        # Jab tak dono strings ke aakhir tak na pahunch jayein
        while i < len(s) and j < len(t):
            # Agar characters match ho jayein, s ka pointer aage badhao
            if s[i] == t[j]:
                i += 1
            # t ka pointer hamesha aage badhega
            j += 1
            
        # Agar i poora len(s) tak pahunch gaya, toh saare letters mil gaye
        return i == len(s)