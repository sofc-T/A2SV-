# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curN = None, head
        while curN:
            nex = curN.next
            curN.next = prev
            prev, curN =curN, nex
        return prev