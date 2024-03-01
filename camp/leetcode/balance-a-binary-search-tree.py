# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def traverse(root):
            if not root:
                return []
            return traverse(root.left) + [root.val]  + traverse(root.right)
        
        def divide_conquer(l,r):
            if l > r:
                return
            mid = (r + l)  // 2
            root = TreeNode(nums[mid])

            root.left = divide_conquer(l,mid-1)
            root.right = divide_conquer(mid+1,r)
            return root
        nums = traverse(root)
        return divide_conquer(0,len(nums)-1)