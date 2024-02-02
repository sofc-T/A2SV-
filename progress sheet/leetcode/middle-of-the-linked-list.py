# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        curN , cn = head , head
        while curN.next:
            if curN.next.next:
                curN = curN.next.next
                cn = cn.next
            else:
                break
        if curN.next:
            return cn.next
        return cn