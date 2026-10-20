class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        mapping = {}
        
        # 1. nums2 ke saare elements ke liye Next Greater Element dhoondo
        for num in nums2:
            # Agar current num stack ke top se bada hai, toh top element ka next greater mil gaya!
            while stack and num > stack[-1]:
                mapping[stack.pop()] = num
                
            stack.append(num)
            
        # 2. Jo elements stack mein bache reh gaye, unka koi next greater nahi hai (-1)
        while stack:
            mapping[stack.pop()] = -1
            
        # 3. nums1 ke order mein results map se utha kar return kar do
        return [mapping[num] for num in nums1]