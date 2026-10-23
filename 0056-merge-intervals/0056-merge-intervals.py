class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # Step 1: Intervals ko unke 'start' time ke according sort karo
        # Keyword: key=lambda x: x[0] -> Har sub-list ka pehla element (start time) extraction ke liye
        intervals.sort(key=lambda x: x[0])
        
        # Result list initialize karo
        merged = []
        
        # Step 2: Har interval par iterate karo
        # Keyword: current -> Is loop cycle ka active interval [start, end]
        for current in intervals:
            
            # Line 1: Check karo ki list khaali hai ya overlap NAHI hai
            # Conditions:
            # 1. 'not merged' -> Pehla element array mein direct push hoga
            # 2. 'current[0] > merged[-1][1]' -> Naye interval ka start > Pichhle merged ka end
            if not merged or current[0] > merged[-1][1]:
                
                # Line 2: Koi overlap nahi hai, toh current ko new entry bana ke daal do
                merged.append(current)
                
            else:
                # Line 3: Overlap MIL GAYA! 
                # Pichhle merged interval ka end time update karo
                # Formula: max(purana end, naya end)
                merged[-1][1] = max(merged[-1][1], current[1])
                
        return merged
        # time complexity = o(nlogn)
        #space complexity = o(n)