class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i = 0
        k = 0
        # [2,0,1]
        #. i.   j
        #.      k
        # [ 2, 1 , 0]
        #  i      j 
        #.         k
        #[ 0 , 1 , 2]
        #      i    k 
        #.     j 
        j = len(nums)-1
        while k <= j:
            if nums[k] == 0:
                nums[i],nums[k] = nums[k],nums[i]
                i += 1
                k += 1
            elif nums[k] == 1:
                k += 1
            else:
                nums[k], nums[j] = nums[j], nums[k]
                j -= 1
        """
        Do not return anything, modify nums in-place instead.
        """
        