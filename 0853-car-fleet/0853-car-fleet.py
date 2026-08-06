class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 1. Position aur Speed ko pair karke position ke according sort karo (Descending)
        pair = [[p, s] for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        
        stack = []
        
        # 2. Target ke paas wali car se shuru karke process karo
        for p, s in pair:
            time = (target - p) / s
            stack.append(time)
            
            # Agar peeche wali car ka time aage wali car se kam ya barabar hai,
            # toh wo aage wali fleet mein combine ho jayegi (pop stack)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
                
        # Stack ka length hi total fleets count hoga
        return len(stack)