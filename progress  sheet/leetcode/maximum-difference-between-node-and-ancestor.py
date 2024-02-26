# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def traverse(root,maxx,minn,ans):
            if not root:
                return 0
            maxx = max(maxx,root.val)
            minn = min(root.val,minn)
            ans = max(ans,maxx-minn)
            return max(ans,traverse(root.left,maxx,minn,ans),traverse(root.right,maxx,minn,ans))
        return traverse(root,root.val,root.val,0)
