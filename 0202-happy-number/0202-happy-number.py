class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(number: int) -> int:
            total_sum = 0
            while number > 0:
                digit = number % 10 
                total_sum += digit ** 2
                number //= 10 
            return total_sum
            # 36 / 10 -> 3 -> 0
            # digit = 36+9
            # total_sum = 45
        slow = n
        fast = get_next(n)
        # 19 
        # slow = 19 -> 82 -> 68
        # fast = 19 -> 68 -> 100 -> 1
        # return number is happy
        

        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        
        return fast == 1