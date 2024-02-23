# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:return root2
        if not root2:return root1
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left,root2.left)
        root1.right = self.mergeTrees(root1.right,root2.right)
        return root1
        # def merge(root1,root2):
        #     root1.val += root2.val

        #     if not root1.left:
        #         root1.left = root2.left
                
        #     elif not root2.left:
        #         pass
        #     else:
        #         merge(root1.left,root2.left)
        #     if not root1.right:
        #         root1.right = root2.right
                
        #     elif not root2.right:
        #         pass
        #     else:
        #         merge(root1.right,root2.right)
                
        # merge(root1,root2)
        # return root1