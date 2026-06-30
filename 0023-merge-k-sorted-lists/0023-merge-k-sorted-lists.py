import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        
        heap = []
        
        # 2. Saari lists ke heads ko heap mein daalo (sath mein index 'i' unique rakhne ke liye)
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i, l))
                
        # 3. Jab tak heap khali nahi hota, nodes nikalte raho
        while heap:
            val, i, node = heapq.heappop(heap)
            
            # Naye node ko result list ke aage jodo
            curr.next = node
            curr = curr.next
            
            # 4. Agar us list mein aur elements bache hain, toh agla node heap mein push karo
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
                
        return dummy.next
        