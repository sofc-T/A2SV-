# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        while not head:
            return True
        while not head.next:
            return True
        while not head.next.next:
            return head.val == head.next.val
        forwP = head
        forw =head.next
        forN = forw.next
        back = head
        while back and back.next and back.next.next:
            back = back.next.next 
            forw.next = forwP
            forwP , forw , forN = forw , forN , forN.next           
        if back.next: 
            backF = forw
        else:
            backF = forw
            forwP = forwP.next
        print(forwP.val,backF.val)
        while backF:
            print(forwP.val,backF.val )
            
            if backF.val == forwP.val:
                forwP =forwP.next
                backF =backF.next
                
                continue
            return False
        return True

