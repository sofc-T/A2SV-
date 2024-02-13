# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curN, temp = head, head
        while temp:
            while temp and curN.val == temp.val:
                temp = temp.next
            curN.next = temp
            curN = curN.next
        return head