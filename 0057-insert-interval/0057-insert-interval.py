class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)
        
        # Phase 1: Saare intervals jo newInterval se pehle aate hain aur overlap nahi karte
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
            
        # Phase 2: Saare intervals jo newInterval ke saath overlap kar rahe hain
        while i < n and intervals[i][0] <= newInterval[1]:
            # Interval ko merge karke newInterval ko bada banate jao
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
            
        # Ab merged newInterval ko result mein insert kar do
        result.append(newInterval)
        
        # Phase 3: Baaki bache hue saare intervals jo newInterval ke baad aate hain
        while i < n:
            result.append(intervals[i])
            i += 1
            
        return result