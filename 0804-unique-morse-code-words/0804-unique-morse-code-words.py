class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        # 1. 26 letters ka standard Morse code table
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        # 2. Unique transformations store karne ke liye ek Set banaya
        seen = set()
        
        for word in words:
            transform = []
            for char in word:
                # ord(char) - ord('a') karne se 'a' ke liye 0, 'b' ke liye 1 mil jayega
                index = ord(char) - ord('a')
                transform.append(morse[index])
            
            # List ko string mein badal kar set mein daal diya
            seen.add("".join(transform))
            
        # 3. Set ka size hi unique transformations ki total count hai
        return len(seen)