# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        min_val, max_val = min(p.val,q.val), max(p.val,q.val)
        if root.val >= min(p.val,q.val) and root.val <= max(p.val,q.val):
            return root
        if p.val < root.val:
            return self.lowestCommonAncestor(root.left,p,q) 
        return self.lowestCommonAncestor(root.right,p,q) 
