# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length, curN = 0, head
        while curN:
            length += 1
            curN = curN.next
        normal, add = length // k, length % k
        curN = head
        ans = []
        
        if k >= length:
            while k:
                ans.append(curN)
                if curN:
                    pre = curN
                    curN = curN.next
                    pre.next = None
                k -= 1
            return ans
        while curN:
            temp = normal - 1
            ans.append(curN)
            while curN and temp:
                curN = curN.next
                temp -= 1
            if curN and add:
                add -= 1
                curN = curN.next
            if curN:
                pre = curN
                curN = curN.next
                pre.next = None
        return ans