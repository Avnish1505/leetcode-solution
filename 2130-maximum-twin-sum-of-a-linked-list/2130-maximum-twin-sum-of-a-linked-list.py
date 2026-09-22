# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow
        while curr:
            next = curr.next
            curr.next = prev 
            prev = curr
            curr = next
     # [5,4,2,1]
     #  f    
     #        s
     # max = max(6,6)
     # max = 6
     # time complexity = 0(n)
     #space complexity = 0(1)

        max_twin_sum = 0
        i = head
        j = prev
        while j:
            current_sum = i.val + j.val
            max_twin_sum = max(max_twin_sum, current_sum)
        
            i = i.next
            j = j.next

        return max_twin_sum