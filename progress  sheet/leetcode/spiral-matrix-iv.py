# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        direction = {(0,1):(1,0), (1,0):(0,-1), (0,-1):(-1,0) , (-1,0):(0,1)}
        dir, curN = (0,1), head
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        row, col = 0 , 0
        visited = set()
        while curN:
            if (row,col) not in visited and row != m and col != n and row != -1 and col != -1:
                matrix[row][col] = curN.val
                curN = curN.next
                visited.add((row,col))
            else:
                row, col = row - dir[0], col - dir[1]
                dir = direction[dir]
            row, col = row + dir[0], col + dir[1]
        return matrix
