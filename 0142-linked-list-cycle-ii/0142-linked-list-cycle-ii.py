# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head 
        # Phase 1: Meeting point dhoondo
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
           # Cycle detect ho gayi!
            if slow == fast:
# Phase 2: slow ko head par reset karo
                slow = head
# Dono ko 1-1 step aage badhao jab tak intersect na ho jayein
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
# Ye intersection point hi cycle ka entry node hai
                return slow
   # Agar cycle nahi hai     
        return None