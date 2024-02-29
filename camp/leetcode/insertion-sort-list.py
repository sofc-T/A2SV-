# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        dummy = ListNode("dummy")
        dummy.next = head
        curN = head.next
        while curN:
            temp = dummy
            while temp.next != curN and curN.val >= temp.next.val:
                temp = temp.next
            cnex = curN.next
            if temp.next != curN:
                tlast = temp
                while tlast.next != curN:
                    tlast = tlast.next
                cnex = curN.next
                temp.next,curN.next,tlast.next = curN, temp.next, curN.next
            curN = cnex
        return dummy.next