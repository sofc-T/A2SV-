# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # if not root.left and not root.right: return True
        # ans = []
        # def helper(root):
        #     if not root: return
        #     helper(root.left)
        #     ans.append(root.val)
            
        #     helper(root.right)
        # helper(root)
        # print(ans)
        # for i in range(1,len(ans)):
        #     if ans[i] > ans[i-1]:
        #         continue
        #     return False
        # return True
        def helper(root,minV,maxV):
            if not root: return True
            if minV < root.val < maxV:
                return helper(root.right,root.val,maxV) and helper(root.left,minV,root.val)
            else:return False
        return helper(root,-inf,inf)