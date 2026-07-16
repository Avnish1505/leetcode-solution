class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Array ke aakhri se shuru karenge. 
        # Socho array ke baahar (top floor) do dummy steps hain jinka cost 0 hai.
        first, second = 0, 0
        
        # Hum array ke aakhri element se peeche ki taraf loop chalayenge
        for i in range(len(cost) - 1, -1, -1):
            # Current step ka cost + agle do steps mein se jo sasta ho
            current = cost[i] + min(first, second)
            
            # Pointers ko peeche shift karo agle iteration ke liye
            second = first
            first = current
            
        # Aakhir mein hum index 0 aur index 1 dono se shuru kar sakte hain,
        # isliye dono positions se jo minimum cost aayega, wahi return karenge.
        return min(first, second)