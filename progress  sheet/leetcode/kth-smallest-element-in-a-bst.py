# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def traverse(root):
            if not root:
                return []
            return [root.val] + traverse(root.left) + traverse(root.right)
        vals = traverse(root)
        vals.sort()
        return vals[k-1]