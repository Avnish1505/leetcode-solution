class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0
        write = 0
        n = len(chars)
        
        while read < n:
            char_start = read
            
            # Consecutive same characters count karo
            while read < n and chars[read] == chars[char_start]:
                read += 1
                
            # Current character ko write index par set karo
            chars[write] = chars[char_start]
            write += 1
            
            count = read - char_start
            
            # Agar count 1 se bada hai, toh unke digits write karo
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
                    
        return write