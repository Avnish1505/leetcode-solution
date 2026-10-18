class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Step 1: Frequency tracking map/dictionary banao
        # Keyword: count -> Isme current window ke har character ki frequency store hogi
        count = {}
        
        # Pointers aur variables initialize karo
        left = 0         # Window ka starting index
        max_freq = 0     # Window ke andar kisi single character ki maximum frequency
        max_length = 0   # Final result (longest valid substring length)
        
        # Step 2: Right pointer se window ko aage badhao
        # Keyword: range(len(s)) -> Single pass iteration
        for right in range(len(s)):
            
            # Line 1: Current character ko frequency dictionary mein update karo
            # Keyword: dict.get(key, default) -> Agar key nahi mili toh 0 return karega
            incoming = s[right]
            count[incoming] = count.get(incoming, 0) + 1
            
            # Line 2: Overall highest frequency update karo
            # Note: max_freq humein yeh batata hai ki window mein dominant character kaun sa hai
            max_freq = max(max_freq, count[incoming])
            
            # Line 3: Check karo ki invalid characters kitne hain
            # Formula: Current Window Size - Max Frequency Character Count
            current_window_size = right - left + 1
            
            # Line 4: Agar replacements needed 'k' se zyada ho gaye, window invalid hai
            if current_window_size - max_freq > k:
                
                # Outgoing character ki frequency kam karo aur left pointer aage khiskao
                outgoing = s[left]
                count[outgoing] -= 1
                left += 1
            
            # Line 5: Valid window length ko compare aur update karo
            max_length = max(max_length, right - left + 1)
            
        return max_length