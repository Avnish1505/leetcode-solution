class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # Heaters array ko sort karo binary search lagane ke liye
        heaters.sort()
        m = len(heaters)
        max_radius = 0
        
        for house in houses:
            # Binary search se insertion index find karo
            idx = bisect.bisect_left(heaters, house)
            
            # Right side heater ka distance (agar exist karta hai)
            dist_right = heaters[idx] - house if idx < m else float('inf')
            
            # Left side heater ka distance (agar exist karta hai)
            dist_left = house - heaters[idx - 1] if idx > 0 else float('inf')
            
            # Is house ke liye closest heater ka distance
            closest_dist = min(dist_left, dist_right)
            
            # Global radius update karo
            max_radius = max(max_radius, closest_dist)
            
        return max_radius