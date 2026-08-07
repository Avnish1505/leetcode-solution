# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Slow aur Fast dono ko head se start karo
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next          # 1 step aage
            fast = fast.next.next     # 2 steps aage
            
            # Agar dono pointers same node par mil gaye
            if slow == fast:
                return True
                
        # Agar loop se baahar aa gaye matlab fast None tak pahunch gaya (No cycle)
        return False