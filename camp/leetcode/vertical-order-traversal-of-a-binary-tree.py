# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def traverse(root,col,min_col,max_col,row):
            if not root:
                min_col = min(min_col,col)
                max_col = max(max_col,col)
                return [] ,min_col, max_col
            val1,min_col,max_col = traverse(root.left,col-1,min_col,max_col,row+1)
            val2,min_col,max_col = traverse(root.right,col+1,min_col,max_col,row+1)

            return [[root.val,col,row]] + val1 + val2,min_col,max_col
        vals,min_col, max_col = traverse(root,0,0,0,0)
        # print(vals)
        vals.sort(key=lambda x:x[0])
        vals.sort(key=lambda x:x[2])
        # print(vals)
        cols = max_col - min_col + 1
        ans = [[] for _ in range(cols-2)]
        for val,col,row in vals:
            ans[col+abs(min_col+1)].append(val)
        return ans
        