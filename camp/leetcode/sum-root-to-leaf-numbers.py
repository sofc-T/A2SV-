# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def traverse(root,path):
            path += str(root.val)
            if not root.right and not root.left:
                return [path]
            
            val1 = traverse(root.left,path) if root.left else [] 
            val2 = traverse(root.right,path) if root.right else []
            
            return val1 + val2
        total = 0
        paths = traverse(root,"")
        
        for path in paths:
            total += int(path)
        return total  

