class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Ek timeline array banate hain max constraints ke hisab se (0 to 1000)
        timeline = [0] * 1001
        
        # Step 1: Har trip ke liye pickup aur drop points par change record karo
        for num_passengers, start, end in trips:
            timeline[start] += num_passengers  # Passengers chade
            timeline[end] -= num_passengers    # Passengers utre
            
        # Step 2: Timeline par traverse karke current load check karo
        current_load = 0
        for passenger_change in timeline:
            current_load += passenger_change
            
            # Agar kisi bhi point par load capacity se zyada hua
            if current_load > capacity:
                return False
                
        return True