# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(root):
            if not root:
                return []
            return [root.val] + traverse(root.left) + traverse(root.right)
        vals = traverse(root)
        count = Counter(vals)
        maxx, occ = [], -1 * inf
        for val in count:
            if count[val] > occ:
                maxx = [val]
                occ = count[val]
            elif count[val] == occ:
                maxx.append(val)
            
        return maxx