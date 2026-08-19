class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        remaining_bytes = 0
        
        for num in data:
            # Sirf least significant 8 bits consider karo
            byte = num & 0xFF
            
            if remaining_bytes == 0:
                # Naya character start ho raha hai
                if (byte >> 7) == 0b0:
                    remaining_bytes = 0
                elif (byte >> 5) == 0b110:
                    remaining_bytes = 1
                elif (byte >> 4) == 0b1110:
                    remaining_bytes = 2
                elif (byte >> 3) == 0b11110:
                    remaining_bytes = 3
                else:
                    # Invalid leading byte (e.g., 10xxxxxx ya 11111xxx)
                    return False
            else:
                # Continuation byte strictly 10xxxxxx hona chahiye
                if (byte >> 6) != 0b10:
                    return False
                remaining_bytes -= 1
                
        return remaining_bytes == 0