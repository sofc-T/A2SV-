# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        store = {}
        curN = head
        while curN:
            if curN in store:
                return True
            else:
                store[curN] = 1
                curN = curN.next
        return False