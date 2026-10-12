class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        
        target_sum = k* threshold

        count = 0

        current_sum = sum(arr[:k])
        if current_sum >= target_sum:
            count += 1

        for i in range( k , len(arr)):
            current_sum += arr[i] - arr[i - k]
            
            if current_sum >= target_sum:
                count += 1
        return count
        # 1 2 3 4
        # 0 1 2 3
        # i
        # j
        # k = 3
        # n - k 
        # n = 4 
        # i + k = 3 

        #time complexity = 0(n)
        #space complexity = 0(1)
