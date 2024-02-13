# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        curN = dummy = Node("dummy")
        dummy.next = head
        temp = None
        while curN and curN.next:
            if curN.next.val < x:
                if temp:
                    greater = temp.next
                    newN = curN.next
                    curN.next = curN.next.next
                    temp.next = newN
                    newN.next = greater
                    temp = temp.next
                    continue
            elif not temp:
                temp = curN
            curN = curN.next
        return dummy.next
            