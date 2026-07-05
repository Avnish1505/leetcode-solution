class Solution:
    def findNthDigit(self, n: int) -> int:
        digit_length = 1  # 1-digit, 2-digit, 3-digit etc.
        count = 9         # Us length ke total kitne numbers hain (9, 90, 900...)
        start = 1         # Us category ka starting number (1, 10, 100...)
        
        # Step 1: Range dhoondho ki n kis digit-length wali range mein aata hai
        while n > digit_length * count:
            n -= digit_length * count
            digit_length += 1
            count *= 10
            start *= 10
            
        # Step 2: Exact number dhoondho jiske andar hamari digit hai
        # (n - 1) // digit_length se pata chalega start se kitne aage jana hai
        target_num = start + (n - 1) // digit_length
        
        # Step 3: Us number ke andar exact konsi digit hamara answer hai
        # (n - 1) % digit_length se index nikal jayega
        digit_index = (n - 1) % digit_length
        
        # Number ko string mein badal kar exact character utha lo
        return int(str(target_num)[digit_index])
        