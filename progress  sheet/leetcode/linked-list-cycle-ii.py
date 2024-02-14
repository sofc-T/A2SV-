# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # curN = head
        # seen = set()
        # while curN:
        #     if curN in seen:
        #         return curN
        #     seen.add(curN)
        #     curN = curN.next
        # return None
        if not head or not head.next:
            return None
        turtle, hare = head, head
        while hare and hare.next:
            hare = hare.next.next
            turtle = turtle.next
            if hare == turtle:
                break
        if not hare or not hare.next:
            return None
        # print(hare.val)
        hare = head
        while hare != turtle:
            turtle = turtle.next
            hare = hare.next
        return hare