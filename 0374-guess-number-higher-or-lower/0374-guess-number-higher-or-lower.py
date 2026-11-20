# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        
        while left <= right:
            # Overflow se bachne ke liye standard mid formula
            mid = left + (right - left) // 2
            res = guess(mid)
            
            if res == 0:
                return mid
            elif res == -1:
                # Hamara guess bada hai, left half mein jao
                right = mid - 1
            else:
                # Hamara guess chota hai, right half mein jao
                left = mid + 1
                
        return -1