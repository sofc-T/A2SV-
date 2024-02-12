# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        if not head.next: return None
        ptr1 , ptr2 = dummy, dummy
        while ptr2 and n + 1:
            ptr2 = ptr2.next
            n -= 1
        
        while ptr2:
            ptr2 = ptr2.next
            ptr1 = ptr1.next
        ptr1.next = ptr1.next.next
        return dummy.next