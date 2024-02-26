# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def traverse(root,level):
            if not root: 
                return []
            return [[level,root.val]] + traverse(root.right,level+1) + traverse(root.left,level+1)
        vals = traverse(root,0)
        vals.sort(key = lambda x: x[0])
        ans, idx = [], 0
        while idx < len(vals):
            level = []
            while idx < len(vals) and  vals[idx][0] == len(ans):
                level.append(vals[idx][1])
                idx += 1
            if not len(ans) % 2:
                ans.append(reversed(level))
            else:
                ans.append(level)
        return ans
