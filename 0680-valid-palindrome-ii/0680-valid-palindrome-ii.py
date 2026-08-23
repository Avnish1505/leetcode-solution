class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome_range(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        left, right = 0, len(s) - 1
        
        while left < right:
            # Agar characters match ho rahe hain, aage badho
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                # Mismatch mila: Left skip karo YA Right skip karo
                return is_palindrome_range(left + 1, right) or is_palindrome_range(left, right - 1)
                
        return True