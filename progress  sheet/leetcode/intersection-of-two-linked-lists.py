# Definition for singly-linked list.
# class ListNode:
#     def init(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curra, currb = headA, headB
        seta = set()
        while curra:
            seta.add(curra)
            curra = curra.next
        
        while currb:
            
            if currb in seta:
                return currb
            currb = currb.next