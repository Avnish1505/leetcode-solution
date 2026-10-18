class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0 
        max_freq = 0 
        max_legth = 0
        for right in range(len(s)):
            incoming = s[right]
            count[incoming] = count.get(incoming , 0) +1
            max_freq = max(max_freq , count[incoming])

            current_window_size = right - left + 1
            if current_window_size - max_freq > k:
                outgoing = s[left]
                count[outgoing] -= 1
                left += 1

            max_legth = max(max_legth , right - left + 1)
        
        return max_legth