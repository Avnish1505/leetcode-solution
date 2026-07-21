# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return
            
        # STEP 1: Middle Node Dhoondo
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # STEP 2: Second Half Ko Reverse Karo
        # slow.next se doosri list shuru hoti hai
        second = slow.next
        slow.next = None  # Pehli list ko mid par cut kar do
        
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
            
        # STEP 3: Dono Halves Ko Interleave (Zip) Karo
        first, second = head, prev  # prev ab reversed second-half ka head hai
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        """
        Do not return anything, modify head in-place instead.
        """
        