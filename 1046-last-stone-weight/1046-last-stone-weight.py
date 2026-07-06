class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 1. Saare stones ko negative karo taaki Max-Heap ki tarah kaam kare
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        
        # 2. Jab tak heap mein kam se kam 2 stones hain, game khelo
        while len(max_heap) > 1:
            # Sabse bhaari do stones nikalne hain
            # Kyunki values negative hain, minus laga kar positive bana rahe hain
            stone1 = -heapq.heappop(max_heap) # Heaviest (y)
            stone2 = -heapq.heappop(max_heap) # Second heaviest (x)
            
            # Agar dono barabar nahi hain, toh naya patthar wapas daalo
            if stone1 != stone2:
                remaining_weight = stone1 - stone2
                heapq.heappush(max_heap, -remaining_weight)
                
        # 3. Agar koi patthar bacha hai toh use return karo, warna 0
        return -max_heap[0] if max_heap else 0
        