# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curN1, curN2 = list1 , list2
        dummy = ListNode("dummy")
        curN = dummy
        while curN1 and curN2:
            if curN1.val < curN2.val:
                curN.next = curN1
                curN1 = curN1.next
            else:
                curN.next = curN2
                curN2 = curN2.next
            curN = curN.next
        if not curN1 and curN2:
            curN.next = curN2
        elif not curN2 and curN1:
            curN.next = curN1
        return dummy.next