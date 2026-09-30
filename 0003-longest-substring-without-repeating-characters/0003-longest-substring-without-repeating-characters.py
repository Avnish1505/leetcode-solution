class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        i = 0
        max_len = 0
        for j, char in enumerate(s):
            if char in seen and seen[char] >= i:
                i = seen[char] + 1
            seen[char] = j
            max_len = max(max_len, j-i+1)

        return max_len

        # " b a c d a c b b "
        #                 i
        #                    j
        #.  {,  ,  , ,  ,  , } 
        #   max_len = 4
        # time = 0(n)
        # space complexity = 0(n)