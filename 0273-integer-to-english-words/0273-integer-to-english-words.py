class Solution:
    def numberToWords(self, num: int) -> str:
        # Edge Case: Agar number khud 0 hai
        if num == 0:
            return "Zero"
            
        # Data Mappings
        self.less_than_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", 
                             "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        
        self.tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        
        self.thousands = ["", "Thousand", "Million", "Billion"]
        
        result = ""
        group_idx = 0
        
        # Number ko 3-3 ke chunks mein process karo (Right to Left)
        while num > 0:
            # Aakhri 3 digits nikalo
            chunk = num % 1000
            
            if chunk != 0:
                # 3-digit ka word banao aur uske aage Thousand/Million jodo
                chunk_words = self.helper(chunk)
                if self.thousands[group_idx]:
                    chunk_words += " " + self.thousands[group_idx]
                
                # Result ke starting mein jodo kyunki hum piche se process kar rahe hain
                if result:
                    result = chunk_words + " " + result
                else:
                    result = chunk_words
                    
            num //= 1000
            group_idx += 1
            
        return result

    def helper(self, num: int) -> str:
        """Helper function jo 0 se 999 tak ke numbers ko convert karta hai"""
        if num == 0:
            return ""
        elif num < 20:
            return self.less_than_20[num]
        elif num < 100:
            # E.g., 23 -> Twenty + " " + Three
            rest = self.helper(num % 10)
            return self.tens[num // 10] + (" " + rest if rest else "")
        else:
            # E.g., 123 -> One Hundred + " " + Twenty Three
            rest = self.helper(num % 100)
            return self.less_than_20[num // 100] + " Hundred" + (" " + rest if rest else "")
        