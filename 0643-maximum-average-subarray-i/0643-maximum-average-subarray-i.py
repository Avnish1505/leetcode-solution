class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum
        for i in range(k , len(nums)):
            window_sum += nums[i] - nums[i - k]
            
            max_sum = max(max_sum, window_sum)

        return max_sum / k

        # [ 1 , 12 , [-5 , -6, 50 , 3]]
        #                            i
        #. k = 4
        # window_sum == 51
        # max_sum = 51/ 4 = 12.75000
        #time complexity = 0(n)
        # space complexity = 0(1)