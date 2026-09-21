# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        if not head or not head.next:
            return True 
            
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
            # 1 2 3 4
            #     s
            #          f 
            # 3 4
            # return False


        first = head
        second = prev 

        while second:
            if first.val != second.val:
                return False

            first = first.next
            second = second.next

        return True