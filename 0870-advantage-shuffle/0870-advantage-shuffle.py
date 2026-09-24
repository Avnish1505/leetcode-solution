class Solution:
    def advantageCount(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # 1. nums1 ko sort karo
        nums1.sort()
        
        # 2. nums2 ko uske orijinal index ke saath pair karke sort karo
        # [(val, index)]
        sorted_nums2 = sorted([(val, i) for i, val in enumerate(nums2)])
        
        # Two pointers for nums1
        left = 0
        right = len(nums1) - 1
        
        # Result array size of len(nums1)
        res = [0] * len(nums1)
        
        # nums2 ko sabse bade element se piche se process karo
        for val, original_idx in reversed(sorted_nums2):
            # Agar nums1 ka sabse bada element nums2 ke bada element ko hara sakta hai
            if nums1[right] > val:
                res[original_idx] = nums1[right]
                right -= 1
            else:
                # Nahi hara sakta, toh sabse chota element sacrifice kar do
                res[original_idx] = nums1[left]
                left += 1
                
        return res