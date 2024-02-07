# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverseB(head,tail):
            prev = tail
            curN = nxt = head
            while curN != tail:
                nxt = curN.next
                curN.next = prev
                prev = curN
                curN = nxt
            return prev
        p = temp =ListNode(-1)
        p.next = head

        for i in range(right):
            if i==(left-1):
                preleft = p
            p = p.next
        nex = p.next
        res = reverseB(preleft.next,nex)
        preleft.next = res
        return temp.next
        
        
        