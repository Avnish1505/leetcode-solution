class Solution:
    def reverseVowels(self, s: str) -> str:
        # Vowels ka set (O(1) lookup ke liye uppercase aur lowercase dono)
        vowels = set("aeiouAEIOU")
        
        # String ko list mein convert karo modification ke liye
        s_list = list(s)
        left, right = 0, len(s) - 1
        
        while left < right:
            # Left pointer ko next vowel par lao
            while left < right and s_list[left] not in vowels:
                left += 1
                
            # Right pointer ko previous vowel par lao
            while left < right and s_list[right] not in vowels:
                right -= 1
                
            # Dono vowels ko swap kar do
            s_list[left], s_list[right] = s_list[right], s_list[left]
            
            # Pointers ko move karo
            left += 1
            right -= 1
            
        return "".join(s_list)