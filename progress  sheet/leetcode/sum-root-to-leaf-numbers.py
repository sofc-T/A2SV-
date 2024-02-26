# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def findPath(root,path):
            path += str(root.val)
            if not root.left and not root.right:
                return [path]
            
            val1, val2 = [] , []
            if root.left:
                val1 = findPath(root.left,path)
            if root.right:
               val2 = findPath(root.right,path)

            return val1 + val2

        paths = findPath(root,"")
        total = 0
        for path in paths:
            total += int(path)
        return total

