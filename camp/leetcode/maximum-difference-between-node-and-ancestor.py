# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def findMax(maxx,minn,root,ans):
            if not root:
                return 0
            maxx = max(root.val,maxx)
            minn = min(root.val,minn)
            ans = maxx - minn

            return max(ans,findMax(maxx,minn,root.left,ans),findMax(maxx,minn,root.right,ans))
        return findMax(-1*inf,inf,root,0)
