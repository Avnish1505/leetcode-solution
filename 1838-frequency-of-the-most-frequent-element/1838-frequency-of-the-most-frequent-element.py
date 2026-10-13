class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        left = 0
        window_sum = 0 
        max_freq = 0
        for right , val in enumerate(nums):
            window_sum += val
            while (val * (right - left + 1) - window_sum) > k:
                window_sum -= nums[left]

                left += 1
            max_freq = max(max_freq , right - left + 1)

        return max_freq 

        # time complexity = 0(nlogn)
        # space complexity = 0(1)