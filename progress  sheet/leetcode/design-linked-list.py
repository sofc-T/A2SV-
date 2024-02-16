class Node:

    def __init__(self,val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.dummy = Node("dummy")
        self.head = Node(None)

    def get(self, index: int) -> int:
        curN = self.dummy
        while curN and index > - 1:
            index -= 1
            curN = curN.next
        
        return curN.val if curN else -1

    def addAtHead(self, val: int) -> None:
        temp = self.dummy.next
        self.dummy.next = Node(val)
        self.dummy.next.next = temp
        
    def addAtTail(self, val: int) -> None:
        curN = self.dummy
        while curN.next:
            curN = curN.next
        curN.next = Node(val)
        
    def addAtIndex(self, index: int, val: int) -> None:
        curN = self.dummy
        # if index == 0:
        #     return addAtHead(val)
        while curN.next and index > 0:
            index -= 1
            curN = curN.next
        if not curN.next and index > 0:
            return 
        temp = curN.next
        curN.next = Node(val)
        curN.next.next = temp
        
    def deleteAtIndex(self, index: int) -> None:
        curN = self.dummy
        while curN.next and index > 0:
            index -= 1
            curN = curN.next
        temp = None
        if curN.next:
            temp = curN.next.next
        curN.next = temp

       

        
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)