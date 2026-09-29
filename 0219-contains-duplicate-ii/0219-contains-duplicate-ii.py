class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        window = set()
        for i, num in enumerate(nums):
            if num in window:
                return True
            
            window.add(num)
            if len(window) > k:
                window.remove(nums[i-k])
        return False

        # [1, 2, 3, 1].  k = 3
        #.  0 1  2  3
        #.  i
        #.          j

    # time complexity = 0(n)
    # space complexity = 0(k)