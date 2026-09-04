class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Range set karo 1 se num tak
        left = 1
        right = num
        
        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid
            
            if square == num:
                return True
            elif square < num:
                # Agar square chhota hai, to bade numbers check karo
                left = mid + 1
            else:
                # Agar square bada hai, to chhotay numbers check karo
                right = mid - 1
                
        return False