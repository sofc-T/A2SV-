# Definition for a binary tree root.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        def maxBST(root):
            if not root:
                return [0,True,-inf,inf]
            right = maxBST(root.right)
            left = maxBST(root.left)
            valid = True if left[2] < root.val < right[3] else False
            
            
            if not left[1] or not right[1] or not valid:
                return [0,False,-inf,inf]
            
            
            ans[0] = max(ans[0],root.val + left[0] + right[0])
            return [root.val + left[0] + right[0],valid,max(right[2],root.val),min(root.val,left[3])]
        maxBST(root)
        return ans[0]