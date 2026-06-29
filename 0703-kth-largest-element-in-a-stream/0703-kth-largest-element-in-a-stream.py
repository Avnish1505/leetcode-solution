class KthLargest(object):

    def __init__(self, k, nums):
        self.k = k
        self.heap = nums
        
        # 1. Normal list ko Min-Heap mein badal do
        heapq.heapify(self.heap)
        
        # 2. Heap ka size tab tak chota karo jab tak usme sirf k elements bachein
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    
    def add(self, val):
        # Naya score aaya, heap mein daal do
        heapq.heappush(self.heap, val)
        
        # Agar size k se bada ho gaya, toh min element uda do
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
            
        return self.heap[0]