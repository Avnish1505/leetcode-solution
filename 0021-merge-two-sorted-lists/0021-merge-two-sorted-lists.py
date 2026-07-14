# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Ek nakli dummy node banao aur tail ko wahan set karo
        dummy = ListNode()
        tail = dummy
        
        # 2. Jab tak dono lists mein elements hain, compare karte chalo
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next  # list1 ko aage badhao
            else:
                tail.next = list2
                list2 = list2.next  # list2 ko aage badhao
            
            tail = tail.next  # tail ko naye aakhri node par le jao
            
        # 3. Agar koi ek list bach gayi hai, toh use direct attach kar do
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
            
        # Dummy ka agla node hi hamari asli merged list ka head hai
        return dummy.next
        