class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
         
        unique_nums = sorted(set(nums))

        ans = n 

        for i in range(len(unique_nums)):
            min_val = unique_nums[i]
            max_val = min_val + n - 1

            idx = bisect.bisect_right(unique_nums,max_val)

            count = idx - i

            ans = min(ans, n - count)

        return ans 