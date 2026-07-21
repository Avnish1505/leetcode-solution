class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        
        for num in arr:
            # Check karo ki number odd hai ya nahi
            if num % 2 != 0:
                count += 1
                # Agar 3 consecutive odds mil gaye
                if count == 3:
                    return True
            else:
                # Even number aate hi chain break ho gayi, count reset
                count = 0
                
        return False