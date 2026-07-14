class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # Keyboard ki teeno rows ke sets
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        
        result = []
        
        for word in words:
            # Word ke saare characters ko lowercase karke unka set banao
            word_set = set(word.lower())
            
            # Check karo kya yeh set kisi bhi ek row ka subset hai
            if word_set.issubset(row1) or word_set.issubset(row2) or word_set.issubset(row3):
                result.append(word)
                
        return result
        