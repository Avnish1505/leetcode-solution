class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # 1. Array ko sort karo taaki adjacent elements ka difference nikal sakein
        arr.sort()
        
        min_diff = float('inf')
        result = []
        
        # 2. Pehle loop mein minimum absolute difference dhoodho
        for i in range(1, len(arr)):
            current_diff = arr[i] - arr[i-1]
            if current_diff < min_diff:
                min_diff = current_diff
                
        # 3. Doosre loop mein un saare pairs ko collect karo jinka diff min_diff hai
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == min_diff:
                result.append([arr[i-1], arr[i]])
                
        return result