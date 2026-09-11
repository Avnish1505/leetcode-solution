class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        n = len(s)
        i = 0
        
        while i < n:
            # 1. Skip spaces
            while i < n and s[i] == ' ':
                i += 1
            if i >= n:
                break
                
            # 2. Find the end of the current word
            j = i
            while j < n and s[j] != ' ':
                j += 1
                
            # 3. Extract word and add to list
            words.append(s[i:j])
            i = j
            
        # 4. Reverse words list and join with single space
        return " ".join(words[::-1])