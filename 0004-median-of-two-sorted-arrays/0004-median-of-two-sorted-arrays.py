class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2
        
        # Hamesha chote array par binary search chalao taaki O(log(min(m, n))) ho sake
        if len(B) < len(A):
            A, B = B, A
            
        low, high = 0, len(A)
        
        while low <= high:
            i = (low + high) // 2  # A ka partition index
            j = half - i           # B ka partition index
            
            # Agar index out of bounds hai toh boundary par infinity rakhdo
            A_left = A[i - 1] if i > 0 else float("-infinity")
            A_right = A[i] if i < len(A) else float("infinity")
            B_left = B[j - 1] if j > 0 else float("-infinity")
            B_right = B[j] if j < len(B) else float("infinity")
            
            # Check karo agar sahi partition mil gaya hai
            if A_left <= B_right and B_left <= A_right:
                # Total elements odd hain
                if total % 2:
                    return min(A_right, B_right)
                # Total elements even hain
                return (max(A_left, B_left) + min(A_right, B_right)) / 2
                
            elif A_left > B_right:
                high = i - 1  # A mein left jao
            else:
                low = i + 1   # A mein right jao